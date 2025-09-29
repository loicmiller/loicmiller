---
title: "Securing Workflows Using Microservices and Metagraphs"
authors:
- admin
- Pascal Mérindol
- Antoine Gallais
- Cristel Pelsser
author_notes: []
date: "2021-12-11T00:00:00Z"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-12-11T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*[Multidisciplinary Digital Publishing Institute](https://www.mdpi.com/) (MDPI)*"
publication_short: "*MDPI*"

abstract: Companies such as Netflix increasingly use the cloud to deploy their business processes. Those processes often involve partnerships with other companies, and can be modeled as workflows where the owner of the data at risk interacts with contractors to realize a sequence of tasks on the data to be secured. In this paper, we first show how those workflows can be deployed and enforced while preventing data exposure. Second, this paper provides a global framework to enable the verification of workflow policies. Following the principles of zero-trust, we develop an infrastructure using the isolation provided by a microservice architecture to enforce owner policy. We implement a workflow with our infrastructure in a publicly available proof of concept. This work allows us to verify that the specified policy is correctly enforced by testing the deployment for policy violations, and find the overhead cost of authorization to be reasonable for the benefits. In addition, this paper presents a way to verify policies using a suite of tools transforming and checking policies as metagraphs. It is evident from the results that our verification method is very efficient regarding the size of the policies. Overall, this infrastructure and the mechanisms that verify the policy is correctly enforced, and then correctly implemented, help us deploy workflows in the cloud securely.

# Summary. An optional shortened abstract.
summary: []

tags:
- Data leak
- Workflow
- Microservices
- Authorization
- Access control
- Policy verification
- Metagraphs
- YAWL
- Rego

# Display this page in the Featured widget?
featured: false

hugoblox:
  ids:
    doi: 10.3390/electronics10243087

links: []
  # - type: pdf
  #   url: http://arxiv.org/pdf/1512.04133v1
  # - type: code
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: dataset
  #   url: ""
  # - type: poster
  #   url: ""
  # - type: project
  #   url: ""
  # - type: slides
  #   url: https://www.slideshare.net/
  # - type: source
  #   url: ""
  # - type: video
  #   url: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Loïc Miller**](https://www.mdpi.com/2079-9292/10/24/3087)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---