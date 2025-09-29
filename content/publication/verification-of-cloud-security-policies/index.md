---
title: "Verification of Cloud Security Policies"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Pascal Mérindol
  - Antoine Gallais
  - Cristel Pelsser

# Author notes (optional)
author_notes: []

date: '2021-06-07T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2021-06-20T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *[International Conference on High-Performance Switching and Routing](https://hpsr2021.ieee-hpsr.org/) (HPSR 2021), Paris*
publication_short: In *HPSR2021*

abstract: "Companies like Netflix increasingly use the cloud to deploy their business processes. Those processes often involve partnerships with other companies, and can be modeled as workflows where the owner of the data at risk interacts with contractors to realize a sequence of tasks on the data to be secured. In practice, access control is an essential building block to deploy these secured workflows. This component is generally managed by administrators using high-level policies meant to represent the requirements and restrictions put on the workflow. Handling access control with a high-level scheme comes with the benefit of separating the problem of specification, i.e. defining the desired behavior of the system, from the problem of implementation, i.e. enforcing this desired behavior. However, translating such high-level policies into a deployed implementation can be error-prone. Even though semi-automatic and automatic tools have been proposed to assist this translation, policy verification remains highly challenging in practice. In this paper, our aim is to define and propose structures assisting the checking and correction of potential errors introduced on the ground due to a faulty translation or corrupted deployments. In particular, we investigate structures with formal foundations able to naturally model policies. Metagraphs, a generalized graph theoretic structure, fulfill those requirements: their usage enables to compare high-level policies to their implementation. In practice, we consider Rego, a language used by companies like Netflix and Plex for their release process, as a valuable representative of most common policy languages. We propose a suite of tools transforming and checking policies as metagraphs, and use them in a global framework to show how policy verification can be achieved with such structures. Finally, we evaluate the performance of our verification method."

# Summary. An optional shortened abstract.
summary: []

tags:
  - Policy verification
  - Metagraphs
  - Policy modeling
  - Rego
  - Access control
  - Authorization

# Display this page in the Featured widget?
featured: false

# Standard identifiers for auto-linking
hugoblox:
  ids:
    doi: 10.1109/HPSR52026.2021.9481870

# Custom links
links:
  # - type: pdf
  #   url: ""
  # - type: code
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: dataset
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  - type: slides
    url: verification-of-cloud-security-policies-slides.pdf
  # - type: source
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: video
  #   url: https://youtube.com

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/fr/photos/statue-en-beton-blanc-dun-homme-PEWUJV_saKI)'
  focal_point: ''
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