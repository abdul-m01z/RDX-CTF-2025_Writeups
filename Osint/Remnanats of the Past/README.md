## **“Remnanats of the Past”**

**Author:** Huzaifa Zia



## 🎯 Objective

The player must discover a hidden flag by tracing a digital trail through:

* Image metadata
* Social media
* Wireless geolocation
* GitHub commit history

---

## 🟢 Step 1: EXIF — The First Clue

Participants receive a mysterious image (e.g., `xoxo.png`). On inspecting the **EXIF metadata** with `exiftool`, they uncover:

```txt
Owner Name   : abbug786  
Platform     : to be used on X
```

🔍 This directs solvers to the **Twitter (X)** handle `@abbug786`.

---

## 🟡 Step 2: Twitter Profile — Three Layers of Clues

### 🔐 A. Location Field:

```txt
“true code lies in X_Y”
```

✅ Hint that the **GitHub repository name will be coordinates in X\_Y format**.

---

### 🧪 B. Bio Base64:

```
dGhlIG5leHQgcGllY2UgbGllcyBidXJpZWQgaW4gdGhlIHJ1aW5zIG9mIGFuY2llbnQgVGFrc2hhc2hpbGEu
```

Decoded:

```
the next piece lies buried in the ruins of ancient Takshashila.
```

This confirms that the correct BSSID should lead to **Taxila** (ancient Takshashila).

---

### 🛰️ C. Tweet with CSV Dump:

```csv
SSID,BSSID,Signal,Channel  
CafeTxlNet,12:E0:61:AA:E8:0D,-50,6  
isb-Admin,12:E0:61:BA:E8:0C,-60,11  
lhr-FreeWiFi,12:E0:61:AA:E8:0C,-45,6 ← ✅  
AncientNexus,1A:E0:61:AA:E8:0C,-49,1  
LibraryNet-Guest,12:E0:61:AA:EA:0C,-70,11
```

🕵️ Red herrings abound, but only one BSSID is valid:
➡️ `12:E0:61:AA:E8:0C`

---

## 🟠 Step 3: WiGLE Geolocation

Using [WiGLE.net](https://wigle.net), players input the correct BSSID and discover:

```
Coordinates: 33.73448563, 72.79516602  
Location: Taxila, Pakistan
```

🧭 These match the clue "Takshashila" from the bio, confirming the correct trail.

---

## 🔵 Step 4: GitHub Repository

Using the final hint:

> “true code lies in X\_Y”

Players locate a GitHub repository titled:

```
33.734_72.795
```

---

## 📂 Step 5: The Final README

Upon opening the repo, players are greeted with this:

```markdown
33.734_72.795  
“Takshashila was never truly lost. Just... encoded.”

The Signal Ends Here  
You've decoded the image, chased signals through the air, followed trails across ancient lands, and landed precisely here — at the axis of 33.734_72.795.

This was once known as Takshashila.

You're now standing on coordinates that haven't whispered their secrets for centuries.

But now...

They speak again.

Look closely. The ruins are never what they seem.

🧩 A final twist: Not all flags are written. Some... just become committed to the past.
```

Players realize they must examine the Git history.

---

## 🟥 Step 6: Git Forensics

Using:

```bash
git log -p
```

They uncover a **flag that was added and then removed** from the `README.md`:

```diff
+ RDX{Takshashila_Whispers_Heard}
```

---

## 🏁 Final Flag:

```
RDX{Takshashila_Whispers_Heard}
```


