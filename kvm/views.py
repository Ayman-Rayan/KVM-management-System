from ast import Return
from multiprocessing import context
from django.http import JsonResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .form import KvmForm
from .models import Kvmm
import libvirt


from .models import Kvmm

def createKvm(request):
    form = KvmForm
    if request.method == 'POST' :
        print('Printing POST : ', request.POST)
        form = KvmForm(request.POST)
        if form.is_valid():
            kvm = form.save(commit=False)
            kvm.kvmcreator = request.user.id
            kvm.save()
            #form.save()
            return redirect('/kvm/list/')
    context= {'form':form}
    return render(request, 'kvm/kvm_form.html', context)
def index(request):  
    kvms = Kvmm.objects.all()  
    return render(request,'kvm/kvm_list.html',{'kvms':kvms}) 

def startKvm(request, id):
    obj = Kvmm.objects.get(id=id)
    print(obj.disk)
    xml = f"""<domain type='kvm'>
    <name>{obj.name}</name>
    <memory unit='KiB'>{obj.memory}</memory>
    <currentMemory unit='KiB'>{obj.memory}</currentMemory>
    <vcpu placement='static'>{obj.vcpus}</vcpu>
    <os>
        <type arch='x86_64' machine='pc-i440fx-focal'>hvm</type>
        <boot dev='cdrom'/>
    </os>
    <features>
        <acpi/>
        <apic/>
        <vmport state='off'/>
    </features>
    <cpu mode='host-model' check='partial'/>
    <clock offset='utc'>
        <timer name='rtc' tickpolicy='catchup'/>
        <timer name='pit' tickpolicy='delay'/>
        <timer name='hpet' present='no'/>
    </clock>
    <on_poweroff>destroy</on_poweroff>
    <on_reboot>restart</on_reboot>
    <on_crash>destroy</on_crash>
    <pm>
        <suspend-to-mem enabled='no'/>
        <suspend-to-disk enabled='no'/>
    </pm>
    <devices>
        <emulator>/usr/bin/qemu-system-x86_64</emulator>
        <disk type='file' device='disk'>
        <driver name='qemu' type='raw'/>
        <source file='{obj.storage}'/>
        <target dev='hda' bus='ide'/>
        <address type='drive' controller='0' bus='0' target='0' unit='0'/>
        </disk>
        <disk type='file' device='cdrom'>
            <driver name='qemu' type='raw'/>
            <source file='{obj.iso}'/>
        <target dev='hdb' bus='ide'/>
        <readonly/>
        <address type='drive' controller='0' bus='0' target='0' unit='1'/>
        </disk>
        <controller type='usb' index='0' model='ich9-ehci1'>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x7'/>
        </controller>
        <controller type='usb' index='0' model='ich9-uhci1'>
        <master startport='0'/>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x0' multifunction='on'/>
        </controller>
        <controller type='usb' index='0' model='ich9-uhci2'>
        <master startport='2'/>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x1'/>
        </controller>
        <controller type='usb' index='0' model='ich9-uhci3'>
        <master startport='4'/>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x2'/>
        </controller>
        <controller type='pci' index='0' model='pci-root'/>
        <controller type='ide' index='0'>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
        </controller>
        <controller type='virtio-serial' index='0'>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>
        </controller>
        <interface type='network'>
        <mac address='52:54:00:25:fc:b8'/>
        <source network='default'/>
        <model type='e1000'/>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
        </interface>
        <serial type='pty'>
        <target type='isa-serial' port='0'>
            <model name='isa-serial'/>
        </target>
        </serial>
        <console type='pty'>
        <target type='serial' port='0'/>
        </console>
        <channel type='spicevmc'>
        <target type='virtio' name='com.redhat.spice.0'/>
        <address type='virtio-serial' controller='0' bus='0' port='1'/>
        </channel>
        <input type='tablet' bus='usb'>
        <address type='usb' bus='0' port='1'/>
        </input>
        <input type='mouse' bus='ps2'/>
        <input type='keyboard' bus='ps2'/>
        <graphics type='spice' autoport='yes'>
        <listen type='address'/>
        <image compression='off'/>
        </graphics>
        <sound model='ich6'>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
        </sound>
        <video>
        <model type='qxl' ram='65536' vram='65536' vgamem='16384' heads='1' primary='yes'/>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
        </video>
        <redirdev bus='usb' type='spicevmc'>
        <address type='usb' bus='0' port='2'/>
        </redirdev>
        <redirdev bus='usb' type='spicevmc'>
        <address type='usb' bus='0' port='3'/>
        </redirdev>
        <memballoon model='virtio'>
        <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>
        </memballoon>
    </devices>
    </domain>
    """
    print(xml)
    conn = libvirt.open('qemu:///session')
    dommain = conn.defineXML(xml) 
    
    if dommain :
            return JsonResponse({"instance": "VM created successfully"}, status=200)
    else:
            return JsonResponse({"instance": "VM not created "}, status=400)
   

def destroyConfirmPage(request, id):  
    vm = Kvmm.objects.get(id=id)  
    return render(request,'kvm/kvm_confirm_delete.html',{'vm':vm}) 

    
def destroy(request, id):  
    vm = Kvmm.objects.get(id=id)  
    vm.delete()  
    return redirect('/kvm/list/')      