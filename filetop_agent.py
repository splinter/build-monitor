import event_client
from bcc import BPF

bpf_text= """
#include <linux/sched.h>
#include <linux/fs_struct.h>
#include <linux/dcache.h>

// define output data structure in C
struct data_t {
    u32 pid;
    u64 ts;
    char comm[TASK_COMM_LEN];
    const char *filename;
};
BPF_PERF_OUTPUT(events);

int on_read(struct pt_regs *ctx, int dfd, const char __user *filename, int flags){
    struct data_t data = {};
    data.filename = filename;
    events.perf_submit(ctx,&data,sizeof(data)); 
    return 0;
}

"""

b = BPF(text=bpf_text)
b.attach_kprobe(event= b.get_syscall_prefix().decode() + 'open', fn_name="on_read")
b.attach_kprobe(event= b.get_syscall_prefix().decode() + 'openat', fn_name="on_read")

def print_event(cpu, data,size):
    event = b["events"].event(data)
    print("Recieved event")
    print(event.filename)

b["events"].open_perf_buffer(print_event)
event_client.start_client()
while 1:
    b.perf_buffer_poll()