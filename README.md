## 💡 Automated Clock Synchronization Project (Ansible & Python)

### Problematic

I have problem with my minipc time. Every I turn on my minipc got failure time because dead of computer CMOS battery. I cannot browsing with my lovely Firefox browser. So with my programming skill. I have been challanged to solve this problem with programming. A Fact i cannot solve this problem with one step but more than that.

### Evolution Problem Solving
1. Create Python script to syncronizing from  Linux Mint to my android device / Termux app
2. Make crontab to schedule python script every booting my computer
3. Combine and integrate a python script and ansible on crontab

### Final Conclusion Step By Step

* Designed and implemented an automated configuration management script using Ansible to synchronize system clocks across local infrastructure.
* Configured a script Python and Ansible on Linux Mint to syncronous time (date hour and minute) on a mobile device environment to act as a local time stratum source.
* Developed OS-specific playbooks (Linux) leveraging module automation (ansible, python) to enforce real-time system clock drift correction.
* Skills Used: Ansible, Infrastructure as Code (IaC), Linux Administration, Networking, and Python .

[Open Directory jam_set](jam_set/)

![Demonstration](video_and_images/demo_automated_clock_synchronization.mp4)


### Other Architectur Server InvenTree Implementation Using Container Docker

```text

       [ PENGGUNA / CLIENT ]
                 │
                 ▼ (Port 8080)
┌─────────────────────────────────────────┐
│          inventree-proxy-pos            │
│               (Caddy)                   │
└──────────────────┬──────────────────────┘
                   │
                   ├───────────────────────────────────┐
                   ▼ (Port 8000)                       ▼ (Read Static Files)
┌─────────────────────────────────────────┐ ┌───────────────────────────────────┐
│          inventree-server-pos           │ │        inventree_data_pos         │
│          (Web Utama: Gunicorn)          │ │         (Shared Volume)           │
└──────────┬──────────────────┬───────────┘ └───────────────▲───────────────────┘
           │                  │                             │ (Media/Static)
           │                  │                             │
           ▼                  ▼                             ▼
┌────────────────────┐ ┌────────────────────┐ ┌───────────────────────────────────┐
│  inventree-db-pos  │ │inventree-cache-pos │ │       inventree-worker-pos        │
│    (PostgreSQL)    │ │      (Redis)       │ │        (Background Worker)        │
└──────────┬─────────┘ └────────────────────┘ └─────────────┬─────────────────────┘
           │                                                │
           ▼                                                ▼
┌────────────────────┐                            ┌────────────────────┐
│inventree_db_data_..│                            │ inventree-db-pos   │
│  (Volume Data DB)  │                            │ inventree-cache-pos│
└────────────────────┘                            └────────────────────┘


┌────────────────────────────────────────────────────────────────────────┐
│ [ SERVER FISIK / VPS / HOST OS ]                                       │
│                                                                        │
│ ┌────────────────────────────────────────────────────────────────────┐ │
│ │ DOCKER ENGINE / RUNTIME                                            │ │
│ │                                                                    │ │
│ │  ┌──────────────────────────────────────────────────────────────┐  │ │
│ │  │ DOCKER NETWORK (Internal Internal Bridge)                    │  │ │
│ │  │                                                              │  │ │
│ │  │  ┌──────────────────────┐          ┌──────────────────────┐  │  │ │
│ │  │  │ [CONTAINER 1]        │          │ [CONTAINER 2]        │  │  │ |
│ │  │  │ inventree-proxy-pos  ├─────────►│ inventree-server-pos │  │  │ │
│ │  │  │ (Image: caddy)       │ (Proxy)  │ (Image: inventree)   │  │  │ │
│ │  │  └──────────┬───────────┘          └────┬─────────────┬───┘  │  │ │
│ │  │             │                           │             │      │  │ │
│ │  │             │ (Read Static)             │ (SQL)       │(Cache)  │ │
│ │  │             ▼                           ▼             ▼      │  │ │
│ │  │  ┌──────────────────────┐          ┌──────────┐ ┌──────────┐ │  │ │
│ │  │  │ [CONTAINER 3]        │          │CONTAINER4│ │CONTAINER5│ │  │ │
│ │  │  │ inventree-worker-pos │          │inventree-│ │inventree-│ │  │ │
│ │  │  │ (Image: inventree)   │          │db-pos    │ │cache-pos │ │  │ │
│ │  │  └──────────┬───────────┘          │(Postgres)│ │(Redis)   │ │  │ │
│ │  │             │                      └─────────┬┘ └─────────┬┘ │  │ │
│ │  └─────────────┼────────────────────────────────┼────────────┼──┘  │ │
│ │                │                                │            │     │ │
│ │                ▼ (Mount Volume)  (Mount Volume) ▼            ▼     │ │
│ │  ┌──────────────────────────────┐     ┌──────────────────────────┐ │ │
│ │  │ DOCKER VOLUMES (Di Host OS)  │     │ DOCKER VOLUMES (Di Host) │ │ │
│ │  │ inventree_data_pos           │     │ inventree_db_data_pos    │ │ │
│ │  └──────────────────────────────┘     └──────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘

```
