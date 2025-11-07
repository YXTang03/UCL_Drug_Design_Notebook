# MEDC0076 Miscellaneous

## October 20: HIV Drug Design

**HIV genetics (RNA)**
$\downarrow$[reverse transcription](#hiv-drug-targets-reverse-transcriptase)
**DNA**
$\downarrow$[integration](#hiv-drug-targets-integrase)
**Host reproduction, transcription, expression**
$\downarrow$[protein modification](#hiv-drug-targets-protease)
**HIV capsids**

### HIV Drug Targets: Reverse Transcriptase

RT has both polymerase and nuclease activities. Drugs targeting RT can either be *nucleoside analogue reverse-transcriptase inhibitors* (NRTIs) or *non-nucleoside reverse-transcriptase inhibitors* (NNRTIs).

### HIV Drug Targets: Integrase

HIV integrase elicits a strand transfer reaction to coporate the reverse transcripted DNA into the host DNA.

### HIV Drug Targets: Protease

The expressed protein is a long polyprotein initially, which must be cleaved by protease to generate proteins with biological activities.

### HIV Drug Targets: Capsid

Capsid function:

- Migrates through the cytoplasm and nuclear envelope to deliver viral DNA to chromatin.
- Protects viral genome from degradation by nucleases and innate immune sensing in the cytoplasm.
- The site of reverse transcription of viral RNA into DNA.
- Bound by a series of host cofactors which regulate reverse transcription and uncoating.

## October 21: Omics

 Human genome mapping can be thought of in different ways:
 1. DNA sequencing – determine the physical position of every base pair in the genome
 2. Functional annotation – determine the location of functional sites in the genome
 3. Mapping variation – sequencing in different populations to determine the sites in DNA that differ between populations (modern definition). Generally, determine the locations of variant regions in the genome
 4. Mapping traits – utilising all the maps above to determine how variations in DNA correlate with variations in traits (**phenotypes**)

Evidence for human genomics as a tool for drug target identification 
- (Drug repurposing) Rediscovery of know drug target-disease pairings 
- (Increase approval rate) Higher rates of approval for drug target-disease indication pairs with genetic support
- (Reveal diseases)Findings from genome wide association studies in specific disease areas
- Successful development of drugs motivated by human genomics
## October 22: Biological Statistics

### Descriptive Statistics

#### Distribution

The frequency of different values of a variable.

#### Central tendency: Mode, Mean, and Median

An estimation of the value at the centre of the distribution.

Different methods are used to describe catagorial and continuous data:

Mode$\rightarrow$catagorial data

Mode, Mean, Median$\rightarrow$continuous data, depending on the shape of the distribution.

#### Dispersion: Range, Interquartile range, and Standard deviation

A measure of the spread of all the values around the central tendency

Interquartile range$\rightarrow$skewed distributions (continuous)
Standard deviation$\rightarrow$normal distributions (continuous)

Standard deviation ($\sigma$):

$\sigma$ measures the spead of values about their mean.

$\sigma \downarrow \quad \rightarrow$ higher consistency

#### Skewness

$$
Skewness \left\{\begin{matrix}
&<0:&\quad Mode > Median > Mean\\
&=0:&\quad Normal\\
&>0:& Mode < Median < Mean
\end{matrix}\right.
$$

### Inferential Statistics

Estimate the population features using sample features.

Null hypothesis ($H_0$, no differences between negative and sample groups)
Alternative hypothesis ($H_1$)

$\alpha$: significance value, set before experiment.
$p\geq \alpha \rightarrow$ accept $H_0$
$p< \alpha \rightarrow$ reject $H_0$ in favour of $H_1$
A larger $\alpha$ value means a lower threshold to reject $H_0$. To illustrate this relationship more clearly, we suppose that $\lim\limits_{\alpha \to 1}$, p-value cannot excess $\alpha$ at any case, which equivalents to $p<\alpha$ constantly and always rejects $H_0$.

Type 1 ($\alpha$) error: Wrongly reject $H_0$, low specificity.
Type 2 ($\beta$) error: Wrongly accept $H_0$, low sensitivity.

#### Parametric/Non-parametric Hypothesis

Known population mean and variance$\rightarrow$ Parametric

Unknown population mean or small population size$\rightarrow$ Non-parametric

#### One/Two sample

#### One-tailed/ Two-tailed

#### ANOVA

More than two groups, avoid serial t-test

### Regression

$$
r\left\{\begin{matrix}r\to 1& \rightarrow Positively\quad correlated\\
r\approx 0&\rightarrow No\quad correlation\\
r \to -1&\rightarrow Negatively\quad correlated
\end{matrix}\right.
$$
