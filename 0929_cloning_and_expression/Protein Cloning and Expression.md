# Protein Cloning and Expression

## Why We Need Cloning?

- Exploit the expression capabilities for large scale production.
- Work with the intended protein directly, instead of its orthologs.
- Highly customizable property make it possible to add tags, purify the protein easily.
<br>
- Cost-effective.
- No risk of contamination by pathogens present in source material.

Research on the application of protein itself:

- Proteins as therapeutics in their own right.
- Diagnostic molecules.

Proteins as targets:

- Investigation in the involvement in a disease of interest

## Process

![alt text](image.png)

Main procedures include:

- [Isolate gene](#isolate-the-gene-of-interest)
- [Clone the gene into a vector](#clone-the-gene-into-a-vector)
- [Transfer](#transfer-into-a-host)
- Extract and purify the protein

### Isolate the Gene of Interest

There are two methods to isolate gene from organisms: using cDNA libraries and using genomic DNA libraries.

cDNA library refers to the gene sourced from reverse transcription of mRNA. A very straightforward feature is  obtained genes do not have introns and reflect what is transcribed.

Genomic DNA library is another situation: introns are included because genes obtained through this method come from chromosome. Meanwhile, regulatory genomic regions of DNA, along with other non-coding regions are also reserved.

#### Codon Optimisation

One thing to note is that **tRNA abundance discrepancies**[^1] are often observed between the gene source organisms and the expression hosts. This difference further changes the translation rate directly, and may lead to protein misfolding or protein aggreation[^2]. Thus, **codon optimisation** is very necessary.

![alt text](image-7.png)

Other factors, such as the possible containing restriction enzyme cutting site in inserted gene, are also the reasons why a codon optimisation is needed.

### Clone the gene into a vector

Vector is a circular autonomously replicating DNA element. The most often used vector is the E.coli plasmid.

There are two kinds of vectors: Expression vector and Cloning vector. The two kinds of vectors often do not co-exist in the same colony, unless extra complex [procedures](#choose-different-antibiotics) are executed. Differences between expression vectors and cloning vectors are shown below.

|Features|Cloning Vector|Expression Vector|
|---|---|---|
|Function|Used to cloning, and reserving recombinant DNA|Expressing proteins|
|Promoters|Weak or None|Strong and controllable. Commonly used promoters include T7|
|Tags|N/A|Owing tags|

#### Components in vectors

##### Antibiotic marker

Add an antibiotic marker to force the cell to maintain the inserted DNA element.

###### Choose different antibiotics

Some antibiotics are more strict in terms of selective pressure they put cells under. Use these antibiotics in case of expressing host unfavorable genes. Commonly used antibiotics are ampicillin, kanamycin, chloramphenicol.

Maintain more than one plasmid at one time.

##### Multiple cloning site (MCS)

MCS is a region in cloning vector which does not exist in the wild type E.coli. Rather, it is engineered by human and **contains numerouse specific DNA sequences recognised by restriction enzymes**. Meanwhile, the original restriction enzyme system in E.coli is destructed. So that it will not degrade the inserted region.

There is a strategy to identify whether a gene sequence has been correctly inserted into MCS called '<font color='steelblue'>blue</font> <font color='white'>white</font> selection'.

    MCS before recombinant -express-> One kind of protein -add specific substrate-> Become blue

    MCS with inserted sequence -> Fail to express that kind of protein -> No colour change when substrate added.

###### Restriction enzymes

Restriction enzymes are an array of enzymes recognising specific DNA sequences and hydrolysing the phosphodiester bonds. Various types of cutting ends, such as blunt end, 3'/5' overhang, single-strand overhangs, can be attained after the process of restriction enzymes.

#### Other cloning strategies

Ligation-independent cloning
Non-enzymatic approaches

#### Additional elements in prokaryotic expression system

Typically have:

- Inducible promoter such as T7 promoter or lac promoter.
- lacl: lac repressor protein, to stronly repress baseline expression. It is useful to handle toxic expressions so that leaky expression will not kill hosts.
- Solubility tag: highly stable and quickly folding tags can stimulate the expressed proteins fold while inhibiting aggregation.
- TEV tag: very specific to protease, allowing remove tags before or after purification.

![alt text](image-8.png)
Shown is the prokaryotic expression system regulated by the lac operator.

Some promoters might be too expressive, causing nascent nucleic acids sequences do not have enough time to fold then aggregate.

#### Problems may occur

![alt text](image-9.png)

#### Miscellaneous

Express gene at hosts' log phase, unless the expressed protein is toxic.

There are also some kinds of proteins hard to recombinant in E.coli such as *transmemberane proteins*.

### Transfer into a host

Transformation is the process by which foreign DNAs are introduced in bacteria cell. This process can be achieved through **chemical** (osmotic pressure) or **electroporation**.

#### Transient transfection or stable transfection

Transient transfection: do not use an introducer to integrate DNA elements into the host DNA.

Stable transfection: On the contrary.

#### Transfer into a mammalian vector

|Advantages|Disadvantages|
|---|---|
|Correct glycosylation|Time consuming|
|Chaperones assist in proper folding| Cell culture can only be performed for a finite amount of time|
|Cells secret proteins into medium|Costly|

[^1]: Some tRNAs are used preferentially in highly expressed genes.
[^2]: Nascent peptide chains find their conformation while they are being produced.
