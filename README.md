# opendaylight-mediawiki-migration
This is an automated simple mediawiki extractor and conversion to rst format.

## Current Functionalities

- Pass any valid mediawiki api URL and it will extract only the media-wiki content and store it in a file which will be converted to rst through pandoc.

*Example*

```

<api>
  <style type="text/css" id="night-mode-pro-style"/>
  <link type="text/css" rel="stylesheet" id="night-mode-pro-link"/>
  <query>
    <normalized>
      <n from="Project_Proposals:USC" to="Project Proposals:USC"/>
    </normalized>
  <pages>
    <page ns="0" title="API" missing=""/>
    <page pageid="2201" ns="180" title="Project Proposals:USC">
       <revisions>
          <rev user="Helenc878" timestamp="2015-01-22T18:03:12Z" comment="change Helen's username" contentformat="text/x-wiki" contentmodel="wikitext" xml:space="preserve">
                == Name == Unified Secure Channel == Repo Name == usc == Description == In enterprise networks, more and more controller and network management systems are being deployed remotely, such as in the cloud. Additionally, enterprise networks are becoming more heterogeneous - branch, IoT, wireless (including cloud access control). Enterprise customers want a converged network controller and management system solution. <big>'''Typical Future Enterprise Networks'''</big> [[File:EnterpriseTopo.png|780x500px|frameless|center|Typical Future Enterprise Networks]] == Use Cases == === Use case 1: Call Home === '''<big>Network edge initiates the communication to the controller (NMS)</big>''' '''Scenario:''' The network edge may be deployed behind a NAT or a firewall, thus the initiation of the session between the controller and network edge has to be from the network edge side; otherwise NAT/FW may drop the session setup request from controller side due to lack of proper states. '''Challenges:''' * Not all existing protocols provide call home mechanism, such as telnet, vnc, snmp etc.; * Future network service protocols are mandatorily required to provide call home mechanism if it’s server side is on devices. [[File:USC Call Home.png |780x500px|frameless|center|Call Home]] === Use case 2: Two-way authentication === '''Scenario:''' Rogue controller may behave as normal controller and respond to devices’ connection request; '''Challenges:''' * Some existing protocols don’t provide solid two-way authentication, such as CAPWAP, SNMP etc.; * The network edge should also authenticate the controller for its following management and service provisioning. [[File:2wayauthentication.png |780x500px|frameless|center|Two Way Authentication]] === Use case 3: Unified channel and single-point authentication === '''Scenario:''' Multi-protocol connections between network edge and controller: ** Set up and maintain connections for each protocol; ** Provide different authentication and security mechanism; '''Challenges:''' * Various connections to handle, secure channel cannot be reused. * No consistent and trusted security guarantee; * Repetitious authentication between a single device and controller [[File:USCUnified.png|780x500px|frameless|center|Unified Channel]] == Solution == A unified secure channel for management and service provisioning [[File:USCSolution.png|780x500px|frameless|center|Solution]] == Architecture == [[File:USCArchitecture.png|780x500px|frameless|center|Architecture]] == Scope == Build a unified secure communication tunnel between network element and controller 1. Create a secure channel 1.1 Allow two-way initiation: Initiate the setup from either one of network element or Controller 1.2 Allow two-way authentication 2. Create a generic mechanism to support various communication protocols 2.1 Invisible to protocols carried 2.2 Multiple protocols share the same tunnel == Resources Committed (developers committed to working) == * Helen Chen [mailto:helen.chen@huawei.com helen.chen@huawei.com] * Jinzhu Duan [mailto:duanjinzhu@huawei.com duanjinzhu@huawei.com] * Xin Chang [mailto:xin.chang@huawei.com xin.chang@huawei.com] * George Zhao [mailto:george.y.zhao@huawei.com george.y.zhao@huawei.com] * An Ho [mailto:an.ho@huawei.com an.ho@huawei.com] * Victor Xu [mailto:s.xu@huawei.com s.xu@huawei.com] * Yan Zhuang [mailto:zhangyan.zhang@huawei.com zhangyan.zhang@huawei.com] == Initial Committers == * Helen Chen [mailto:helen.chen@huawei.com helen.chen@huawei.com] Username: helenc878 * Jinzhu Duan [mailto:duanjinzhu@huawei.com duanjinzhu@huawei.com] Username: djz * Xin Chang [mailto:xin.chang@huawei.com xin.chang@huawei.com] Username: XChang * George Zhao [mailto:george.y.zhao@huawei.com george.y.zhao@huawei.com] Username: gzhao * An Ho [mailto:an.ho@huawei.com an.ho@huawei.com] Username: Anipbu * Victor Xu [mailto:s.xu@huawei.com s.xu@huawei.com] Usernmae: Victorxu * Yan Zhuang [mailto:zhuangyan.zhuang@huawei.com zhuangyan.zhuang@huawei.com] Username: Yan == Vendor Neutral == * No vendor package names in code * No vendor branding present in code or output of build * No vendor branding present in documentation == Meets Board Policy (including IPR) == == Reference == [[File:Odl-usc-2014 11 20.pdf|thumbnail|left|USC Slide deck]]
          </rev>
        </revisions>
      </page>
    </pages>
  </query>
</api>

```

So we want only the content residing between <rev> </rev> and extract it and store it in our local machine.

The `extractor.py` does exactly this thing.

## TODO
Parse the links to be extracted in an automated fashion instead of passing every link name to the list.


## FYI

[Media Wiki API](https://www.mediawiki.org/wiki/API:Main_page)
[OpenDaylight API](https://wiki.opendaylight.org/api.php)
