# Reinvent personalization with Generative AI on Amazon Bedrock: Task decomposition for agentic workflows following human-curated guidelines

## Introduction

This repository contains the code and resources for the AWS Machine Learning Blog post titled "Reinvent personalization with Generative AI on Amazon Bedrock: Task decomposition for agentic workflows following human-curated guidelines". The post demonstrates a unique approach to using large language models (LLMs) for website personalization, tailored to a business's profile, offerings, and industry challenges.

## Solution Overview

The solution decomposes the complex task of website personalization into smaller, more specific sub-tasks performed by specialized agents (LLMs). This approach ensures that the resulting website adheres to the company's guidelines, messaging, and related rules, while incorporating industry pain points, user experience (UX) and user interface (UI) design systems, and human-curated elements.

The solution is demonstrated by applying it to a fictional business consulting company, OneCompany Consulting, which uses LLMs to build personalized marketing content, including text, images, and code for HTML, CSS, and JavaScript.

## Prerequisites

To follow along with this repository, you need the following prerequisites:

- An AWS account
- AWS Command Line Interface (AWS CLI) installed
- Python and the AWS SDK for Python (Boto3) set up
- Amazon SageMaker Studio or Studio Domain
- Model Access in Amazon Bedrock (Stable Diffusion XL, Claude v3-Sonnet, and Claude v3-Haiku)
- Knowledge Base for Amazon Bedrock (instructions provided in the blog post)

## Usage

1. Set up the prerequisites as mentioned in the blog post.
2. Clone this repository or download the provided Jupyter notebook.
3. Follow the step-by-step instructions in the Jupyter notebook to run the personalized website generation process.

The notebook will guide you through the following steps:

- Converting the client profile to natural language
- Retrieving related industry insights using a Retrieval Augmented Generation (RAG) framework
- Generating a detailed website description and visual element descriptions using a personalizer LLM (Claude Sonnet)
- Creating visual assets using an image generator LLM (Stable Diffusion)
- Generating the HTML, CSS, and JavaScript code for the personalized website using a frontend developer LLM (Claude Haiku)
- Deploying the generated website assets to an Amazon S3 bucket

## Data and Sources of Truth

The repository includes fictitious references and data sources created manually or generated using non-Claude language models. These resources serve as examples and should be replaced with your own company guidelines, design systems, and industry-specific data in real-world scenarios.

## Clean up
To clean up the resources created during the walkthrough, follow the instructions provided in the "Clean up" section of the blog post.

## Discussions and Enhancements

The blog post discusses potential enhancements and considerations for further improving the solution, such as batch processing, clustering visitor profiles, providing website templates and chain-of-thought descriptions, and retrieving existing images and icons from the company repository.

## Conclusion

This repository accompanies the AWS Machine Learning Blog post and demonstrates how to use Amazon Bedrock and task decomposition to build personalized website experiences that follow company guidelines and design systems. Refer to the blog post for detailed explanations and insights.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.