# Protein Purification

## Before Purification

**To investivate:**

1. Protein size (MW)
2. Suface charge
3. Surface hydrophobicity
4. Ligand Binding

**OR:** Tag engineering

## **Methods**

### **SDS-PAGE**

> **Protein + SDS** -> **Protein Denatured**, and coated with SDS (eliminate charge difference) -> **Immigration speed is determined by molecular weight only**.

### **Western Blot**

Transfer protein bands from ge to a memberane. Immoblize and detected by specific antibody.

### **Chromatography**

Characteristic absorb wavelength of protein: aromatic rings, cystines and disulphide bonds absorb 280nm UV light.

## **Protein Purification Steps**

### **Step1: Collect proteins**

Operations include harvesting cell by centrifugation, lysing cells in a protease inhibitor cocktail, removing cell debris by centrifugation (different rpm).

### **Step2: Capture**
large sample volume, quick-and-dirty, little product loss
#### Methods: Size exclusion chromatography: 

Capture proteins basing on their [size (MW) difference](#before-purification)

- High resolution but poor column volume. Target proteins might be diluted in power during this process, which limits its applicatioin in the first capture step, but be an option in the last polishing step.

#### Methods: Ion exchange chromatography: 

Capture proteins basing on their [different surface charge](#before-purification).

- Eluting the bound proteins out using salt solution with higher ionic intensity
- Large column volume and high resolution. IEC can be applied in either the capture step or polishing step.

#### Methods: [Hydrophobic chromatography](#before-purification)

>利用蛋白质的疏水性，蛋白经变性处理或处于高盐环境下疏水残基会暴露于蛋白表面，不同蛋白疏水残基与固定相的疏水性配体之间的作用强弱不同，依次用从高至低离子强度洗脱液可将疏水用作由弱至强的组分分离。

#### Methods: [Affinity chromatography](#before-purification): 

Target proteins, or engineered target proteins, bind to stationary phase covalently. e.g. IMAC[^1] (imobilised metal ion chromatography) is used to capture histidine, cystine, or tryptophan rich proteins. One often used peptide sequence in IMAC is 6-His tag.

### **Step3: Intermediate step** (remove contaminants)

- Aiming to remove **bulk** contaminants.

- Suitable methods include *ion exchange chromatography* (IEC) and *hydrophobic interaction chromatography* (HIC)

### **Step4: Polishing** (something like refinement? remove contaminants too)

- Aiming to remove **difficult** contaminants, such as protein aggregates of the target protein.

- Methods include **SEC** for aggregates of the target protein and high resolution **IEC** for impurities with similar size.

> **one problem in quiz is shown below:**
> Above is an illustration of the X-ray structure of C-reactive protein (CRP). It is a plasma protein that exists in vivo as a pentameric disc consistent with the X-ray structure. Each subunit of CRP has a molecular weight of 25 kDa. During a purification of CRP you will use SEC as the polishing step and SDS-PAGE to analyse the peaks. Both SEC and SDS-PAGE give an estimate of molecular weight. What molecular weights would you expect for SEC and SDS-PAGE?
> Select one or more:
> a.SEC: 25 kDa,  SDS-PAGE: 25 kDa.
> b.SEC: 125 kDa,  SDS-PAGE: 25 kDa.
> c.SEC: 125 kDa, SDS-PAGE: 125 kDa
> d.SEC: 25 kDa, SDS-PAGE: 125 kDa
> e.SEC: 50 kDa, SDS-PAGE: 25 kDa

The correct answer is only `b`, but I thought option `e` should be included, given that subunit dimer, which have a different molecular weight, may also present after SEC.

[^1]: A workflow of the IMAC capture is shown below: **Tag engineering**: Add a 6-His tag on the target protein, along with a TEV cleavage sequence (so that this tag can be removed through TEV, which is very sepecific, easily) -> **IMAC capture** -> **Remove 6-His tag** -> Recover free target protein, with tag binded protein being retained on the stationary phase.
