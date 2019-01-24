#   Innovation Lab(CS299) Project: 

## Quora-Question-Pairs:

#### Problem Statement:

Quora is a place to gain and share knowledge—about anything. It’s a platform to ask questions and connect with people who contribute unique insights and quality answers which empowers people to learn from each other. Over 100 million people visit Quora every month, so it's no surprise that many people ask similarly worded questions. Multiple questions with the same intent can cause seekers to spend more time finding the best answer to their question and make writers feel they need to answer multiple versions of the same question.

More formally, the duplicate detection problem can be defined as follows: given a pair of questions q1 and q2, train a model that learns the function:
 
 f(q1, q2) → 0 or 1 
 
where 1 represents that q1 and q2 have the same intent and 0 otherwise.

#### Aim: 

We aim to develop machine learning and natural language processing systems to automatically identify when questions with the same intent have been asked multiple times on Quora. Doing so will make it easier to find high-quality answers to questions resulting in an improved experience for Quora writers, seekers, and readers.

#### Requirements:
Dataset used for the project is available on [Training DataSet](http://qim.fs.quoracdn.net/quora_duplicate_questions.tsv) (released by Quora itself). It consists of over 400,000 lines of potential question duplicate pairs. Each line contains IDs for each question in the pair, the full text for each question, and a binary value that indicates whether the line truly contains a duplicate pair.
