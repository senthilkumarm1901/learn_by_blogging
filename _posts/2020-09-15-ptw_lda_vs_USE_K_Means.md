---
toc: false
title: Comparing Two Unsupervised Clustering Algorithms for Text Data
layout: post
description: A Short Study comparing PTW_LDA and Transfer Learning powered KMeans on Text Data
categories: [Topic Modeling, LDA, Seeded LDA, Universal Sentence Encoder, KMeans]
image: images/LDA_vs_KMeans/data1_evaluation_complete.PNG
---
## A Study comparing two unsupervised clustering algorithms
- **Prior-topic words** guided *Latent Dirichlet Allocation* and 
- **Universal Sentence Encoder** powered *K-Means*

<details>
<summary> :ballot_box_with_check: 1. <code>Motivation</code> behind Study  </summary>
<br>
  
**Is LDA worthwhile?**
- given that USE can encode complex semantic information <br>

**Can LDA be used for at least some type of data?** 
- where it can produce better/on-par results compared to USE-K-Means
</details>

Before diving into the study, <br> let us understand how **USE-KMeans** and **PTW-guided LDA** works 

<details> 
  <summary> 
    :ballot_box_with_check: 2. Briefly about <code>USE</code> </summary>
<details> 
  <summary> <code>How USE works?</code></summary>
  
![USE](https://www.learnopencv.com/wp-content/uploads/2018/11/Universal-Sentence-Encoder.png) <br>
    
![](https://2.bp.blogspot.com/-9Qk1fubLpzg/Wv2QGgKVVmI/AAAAAAAACvs/Gm-XF3prXVIIvaIkrTmkcIcYz-4qSxLKwCLcBGAs/s400/image2.png) <br>
    
![](https://1.bp.blogspot.com/-w2kAi39zPrE/Wv2OPHTwDgI/AAAAAAAACvY/aQzvBcaIqYkw8McCBcXlTx0pj9FbILH0ACLcBGAs/s400/image4.png) <br>

</details>
<details> 
  <summary> <code>How is USE trained?</code> </summary>
    
![](https://amitness.com/images/use-overall-pipeline.png)

<details> 
  <summary> 1. Skip-thought prediction </summary>

![](https://amitness.com/images/nlp-ssl-neighbor-sentence.gif)

</details> 
<details>
<summary> 2. Response Prediction </summary>

![](https://3.bp.blogspot.com/-qcqYQcxfLS0/Wv2Pxmm945I/AAAAAAAACvk/decC5VtlRGUdD4NqCui3HgNd3LXdjEvlgCLcBGAs/s640/image3.gif)

</details>
<details>
<summary> 3. Natural Language Inference </summary>

![](../docs/images/markdown_table1.PNG)

</details>
</details>
</details>
<details> 
  <summary> :ballot_box_with_check: 3A. Briefly about <code>LDA</code> </summary> 
    <details> 
      <summary> <code>Latent</code> </summary> 
  
  Topic structures in a document are **latent/hidden** in the text.
  
  </details> 
    <details> 
      <summary> <code>Dirichlet</code> </summary> 
      
  The **Dirichlet** distribution determines the mixture proportions of <br> 
        i) the topics in the documents and <br>
        ii) the words in each topic.
    </details> 
    <details>
      <summary> <code>Allocation</code> </summary> 
  **Allocation** of words to a given topic and allocation of topics to a document
  
  </details>    

<details> 
  <summary> <code>Intuitive understanding of Dirichlet Distribution</code> </summary>

- A Normal/Gaussian distribution is a probability distribution over all the real numbers.It is described by a mean and a variance.

![](https://upload.wikimedia.org/wikipedia/commons/7/74/Normal_Distribution_PDF.svg)

- A Poisson Distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval 

![](https://upload.wikimedia.org/wikipedia/commons/1/16/Poisson_pmf.svg)

- Now, what is Dirichlet Distribution? <br>
- The dirichlet distribution is a probability distribution as well <br>
- but it is not sampling from the space of real numbers. Instead it is sampling over a probability simplex <br>

```
 (0.6, 0.4)
 (0.1, 0.1, 0.8)
 (0.05, 0.2, 0.15, 0.1, 0.3, 0.2)
```

![](../docs/images/dirichlet_distribution_of_words_topics.PNG)

**How Dirichlet Distribution varies w.r.t dirichlet prior**
- The below image shows Dir(α) <br>
- As α increases from 0.05 (1/20) to 0.1, 0.2, 0.4 respectively in plots from left to right & top to down, you can see the distribution becoming more uniform. <br>

![](../docs/images/dirichlet_distribution_with_prior.png)

</details>
</details>

<details> 
  <summary> :ballot_box_with_check: 3B. <code>How LDA works (without the math)</code> </summary> 
- LDA is a generative model <br>
- LDA processes documents as 'bag of words' -- ordering of words is not important

![](../docs/images/generative_process_1.png)
<br>
<br>
In principle, LDA generates a document based on **dirichlet distribution (dd) of topics over documents** and **dd of words over topics**

![](../docs/images/generative_process_2.png)

<br>
<br>

But we inverse the generative process for statistical inference

![](../docs/images/generative_process_3.png)

<details> <summary> :ballot_box_with_check: 3C. Understanding the <code>Hyper-parameterspace</code> of LDA</summary> 

![](../docs/images/plate_notation_LDA.png)

D = Total No. of Documents <br>
N = No. of Words = Vocab Size <br>
T = No. of Topics <br>
<br>
θd = Topic Distribution for a particular document d

![](../docs/images/plate_notation_2.png)

<br>
Φt= Word Distribution for a topic t. Here for topic 1 and 2. 

![](../docs/images/plate_notation_3.png)

(colored books represent words/tokens)
 
<br> 
``` 
Zd,n = Topic Distribution for n th word in document d
Wd,n = nth word in dth document
```
<br>

```
α= parameter that sets the dircihlet prior on the per-document topic distribution (θ)
= parameter that represents the doc-topic density
= determines the no. of topics in each doc
= (Default) = 1/num_of_topics (in sklearn and gensim)
decreasing alpha results in less number of topics per document
 
β= parameter that sets the dirichlet prior on the per-topic word distribution (ϕ)
= parameter that represents the topic-word density
= determines the no. of words per each topic
= (Default) = 1/num_of_topics (in sklearn and gensim)
decreasing beta results in just a few major words in topics
 
 
m = base measure for per-document topic distribution; a simplex vector/array (m1, m2, …, mT) ; sums to one
α = Concentration parameter α (positive scalar) 
 
 α * m = (α1, α2, …., αT)
 
 
n = base measure for per-topic word distribution; a simplex vector/array (n1, n2, …, nN); sums to one
β = Concentration parameter β (positive scalar) 
 
 β * n = (β1, β2, …., βT)
 
 
There is also another hyper parameter η - topic coherence or perplexity - which can be used to determine the number of topics 
```

</details>
</details>

<details> <summary> :ballot_box_with_check: 3D. <code>Now, how does PTW-LDA work?</code> </summary> 
- Nudge the regular LDA to converge faster and better with human-reviewed words list for each topic <br>

![](../docs/images/seededlda_1.png)

- How the topics are seeded with some seed words

![](../docs/images/seededlda_3.png)

- Chaotic LDA and Clear PTW_LDA outputs... <br>
- LDA might need several hyperparameter tuning attempts to get to the desired splits <br>
    
<br>
- Default initialization with uniform word topic distribution <br>

![](https://cdn-media-1.freecodecamp.org/images/1*RojQi7m5yBGHSD0Q0HGGYg.png)

- Seeded Initialization

![](https://cdn-media-1.freecodecamp.org/images/1*kMxQ47DFkpxIDBCyXeff6w.png)

- The seeded words are guided towards seeded topics for converging faster

![](../docs/images/simplistic_guided_LDA_notation.PNG)

</details>

<details> 
  <summary> :ballot_box_with_check: 4. <code>Pre-processing and Hyper-parameters</code> that can be tuned </summary> 

**Pre-processing**

| PTW-LDA | USE +   Clustering |  |
|-|-|-|
| 1. Stop words removed | No   pre-processing; Comments were used as is |  |
| 2.   Lemmatized |   |  |
| 3. Top   20 words per (ground truth) label was extracted |   |  |
| 4.   Human-reviewed list of 20 word lists (each corresponding to 1 topic) were   chosen as prior topic words input (SAT is useful when there are prior topic   words fed; otherwise it works as normal LDA) |   |  |


**Hyper-parameters**

| PTW-LDA   (best possible based on heuristics and limited # of experimentations) | USE +   Clustering  |  |
|-|-|-|
| No. Of Topics    | No. Of clusters |  |
| Max Iterations | Max Iterations (for K-Means) |  |
| (default) Doc_topic_prior =   alpha = 1/ no_of_topics |   |  |
| (default) topic_word_prior =   beta = 1/ no_of_topics |   |  |
| Learning_method:   "batch" (whole dataset is used) |   |  |
| (alternative is 'online'   which uses only batch size no. Of comments; similar to mini_batch_kmeans) |   |  |
| Seeded_words_list |  |  |
| Seed_coefficent/seed   confidence (how much to nudge the seeded words) |  |  |

</details>

About the Study <br>

<details> 
  <summary> :ballot_box_with_check: 5. <code>Data</code> Used for this study </summary> 
    
![](../docs/images/data1vsdata2_1.PNG)
![](../docs/images/data1vsdata2_2.PNG)
![](../docs/images/data1vsdata2_3.PNG)

</details> 

<details> 
  <summary> :ballot_box_with_check: 6. Data I - <code>20 Newsgroups</code> - <code>Supervised</code> Evaluation </summary> 

![](../docs/images/data1_evaluation_1.PNG) 
![](../docs/images/data1_evaluation_2.PNG)

</details> 

<details> 
  <summary> :ballot_box_with_check: 7. Data II - <code>ABC Corpus</code> - <code>Unsupervised</code> Evaluation </summary> 

|     Metric    |     PTW-LDA    |     USE-Clustering    |
|-|-|-|
|     Word Embedding   based Coherence Score           |     Coherence   Score for 20 topics: 0.091 <br>     (more the coherence score, better is the clustering output)   <br>    |     Coherence   Score for 20 clusters : 0.159          |
|     Methodology of   computing the above metric    |                Take the top 10         words that constitute each of the 20 topics          (each topic    comprises of a probability simplex of the words; select the top 10 highly    probable words in that topic)      <br>      <br>      For our case, the    top 10 words used for coherence computation in the 10 topics are:       <br>      <br>      [['police',  'baghdad',     'war',  'probe',  'protest',     'anti',  'missing',  'man',     'fight',  'coalition'],    <br>      ['report',  'pm',     'death',  'korea',  'claim',     'war',  'north',  'nt',     'toll',  'protesters'],    <br>      ['win',  'govt',     'set',  'community',  'end',     'wins',  'vic',  'indigenous',  'road',     'help'], <br>      ['world',  'cup',     'australia',  'found',  'ban',     'plans',  'lead',  'gets',     'expected',  'match'],    <br>      ['un',  'coast',     'title',  'takes',  'peace',     'iraq',  'gold',  'defence',     'residents',  'play'],    <br>      ['iraq',  'iraqi',     'war',  'says',  'troops',     'killed',  'dead',  'hospital',  'clash',     'forces'], <br>      ['council',  'boost',     'mp',  'fire',  'group',     'qld',  'minister',  'defends',     'land',  'welcomes'],    <br>      ['man',  'court',     'charged',  'face',  'plan',     'open',  'murder',  'urged',     'case',  'charges'], <br>      ['new',  'oil',     'dies',  'security',  'crash',     'sars',  'high',  'year',     'house',  'car'], <br>      ['water',  'rain',     'claims',  'wa',  'nsw',     'farmers',  'drought',  'howard',     'centre',  'union']] <br>      <br>                   For each topic,         taking 2 out of the top 10 words at a time,  compute cosine similarity using         pre-trained W2V embedding          <br>            Overall         Coherence is sum of similarity scores of all possible pairs of words         for each topic, normalized by the          no. of topics                  |                Take the top 10         words that constitute each of the 20 clusters          (top 10 words    (from stop-words removed set) are computed based on their TF-IDF weighted    scores in that cluster)      <br>      <br>            For each         cluster, taking 2 out of the top 10 words at a time,  compute similarity using pre-trained         W2V embedding          <br>      <br>      For our case, the    top 10 words used for coherence computation in the 10 clusters are:   <br>      <br>     [['win',  'cup',     'final',  'wins',  'world',     'afl',  'coach',  'england',     'season',  'day'], <br>       ['council',     'plan',  'market',  'funding',     'boost',  'housing',  'water',     'funds',  'budget',  'rise'],     <br>       ['crash',     'man',  'killed',  'death',     'dies',  'dead',  'injured',     'woman',  'car',  'sydney'], <br>       ['interview',  'michael',     'business',  'abc',  'news',     'market',  'analysis',  'david',     'extended',  'andrew'],  <br>       ['australia',  'australian',  'aussie',     'sydney',  'australians',  'day',     'aussies',  'australias',  'melbourne',  'south'], <br>       ['abc',     'country',  'hour',  'news',     'weather',  'grandstand',  'friday',     'nsw',  'drum',  'monday'], <br>       ['govt',     'election',  'council',  'government',  'minister',  'pm',     'parliament',  'nsw',  'anti',     'trump'], <br>       ['police',     'man',  'court',  'murder',     'charged',  'accused',  'death',     'guilty',  'charges',  'assault'], <br>       ['farmers',     'water',  'drought',  'industry',  'farm',     'coal',  'green',  'cattle',     'mining',  'nsw'], <br>       ['health',     'hospital',  'flu',  'mental',     'doctors',  'treatment',  'cancer',     'drug',  'service',  'care']] <br>      <br>      <br>            Overall         Coherence is sum of similarity scores of all possible pairs of words         for each cluster, normalized by the          no. of clusters          <br>       |

</details>

<details> 
  <summary> :ballot_box_with_check: 8. <code>Conclusion</code> </summary>

```
We have used two News corpus of varying text length. One dataset has ground truth labels and the other doesn't have labels

```

```
In our comparison of **PTW-LDA vs USE-Clustering**, both based on 'Supervised' and 'Unsupervised' evaluation metrics, USE-clustering performs far superior to PTW-LDA despite repeated attempts at different set of hyper-parameters for PTW-LDA
```
</details>
