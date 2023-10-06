#!/usr/bin/env python
# @lint-avoid-python-3-compatibility-imports
#
# filetop  file reads and writes by process.
#          For Linux, uses BCC, eBPF.
#
# USAGE: filetop.py [-h] [-C] [-r MAXROWS] [interval] [count]
#
# This uses in-kernel eBPF maps to store per process summaries for efficiency.
#
# Copyright 2016 Netflix, Inc.
# Licensed under the Apache License, Version 2.0 (the "License")
#
# 06-Feb-2016   Brendan Gregg   Created this.
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

map = {}
def print_event(cpu, data,size):
    event = b["events"].event(data)
    map[event.name] =1
    
    if(event.name.decode().find("html") > 0):
        print(event.name)
        event_client.log_event(event.name.decode())

b["events"].open_perf_buffer(print_event)
event_client.start_client()
while 1:
    b.perf_buffer_poll()