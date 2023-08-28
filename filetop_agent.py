import event_client
from bcc import BPF

bpf_text= """
#include <uapi/linux/ptrace.h>
#include <linux/blkdev.h>

// define output data structure in C
struct data_t {
    u32 pid;
    u64 ts;
    char comm[TASK_COMM_LEN];
    char name[DNAME_INLINE_LEN];
};
BPF_PERF_OUTPUT(events);

int on_read(struct pt_regs *ctx, struct file * file,char  __user *buf,size_t count,int is_read){

    struct dentry *de = file ->f_path.dentry;
    struct qstr d_name = de->d_name;
    struct data_t data = {};
    bpf_probe_read_kernel(&data.name,sizeof(data.name),d_name.name);
    events.perf_submit(ctx,&data,sizeof(data)); 
    return 0;
}

"""
DNAME_INLINE_LEN = 32
b = BPF(text=bpf_text)
b.attach_kprobe(event= "vfs_read" , fn_name="on_read")
#b.attach_kprobe(event= b.get_syscall_prefix().decode() + 'openat', fn_name="on_read")

def print_event(cpu, data,size):
    event = b["events"].event(data)
    print("Recieved event")
    print(event.name)

b["events"].open_perf_buffer(print_event)
event_client.start_client()
while 1:
    b.perf_buffer_poll()