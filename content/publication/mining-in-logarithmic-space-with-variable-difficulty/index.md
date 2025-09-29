---
title: Mining in Logarithmic Space with Variable Difficulty

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Dorian Pacaud
  - Nathanaël Derousseaux--Lebert
  - Emmanuelle Anceaume
  - Romaric Ludinard

# Author notes (optional)
author_notes: []

date: '2025-10-14T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2025-09-28T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *[ACM Conference on Computer and Communications Security](https://www.sigsac.org/ccs/CCS2025/) (CCS 2025), Taipei*
publication_short: In *CCS 2025*

abstract: "This paper presents the first non-interactive, succinct, and secure representation of a PoW-based blockchain that operates under variable mining difficulty while satisfying both completeness and onlineness properties. Completeness ensures that provers can update an existing NIPoPoW by incorporating a newly mined block, whereas onlineness ensures that miners can extend the chain directly from a NIPoPoW. The time complexity for both the prover (to update a NIPoPoW with a new block) and the verifier is logarithmic in the number of blocks of the underlying PoW blockchain. The communication complexity required for synchronization is polylogarithmic in the length of the blockchain. We prove the correctness of our scheme in the presence of a 1/3-bounded PPT adversary."

# Summary. An optional shortened abstract.
summary: []

tags:
  - Blockchain
  - Variable difficulty
  - Succinct proof
  - Polylogarithmic communication and update complexities

# Display this page in the Featured widget?
featured: true

# Standard identifiers for auto-linking
# hugoblox:
#   ids:
#     doi: hal-05033998

# Custom links
links:
  # - type: pdf
  #   url: ""
  # - type: code
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: dataset
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: slides
  #   url: de-l-utilisation-des-metagraphs-pour-la-verification-de-politiques-de-securite-slides.pdf
  # - type: source
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: video
  #   url: https://youtube.com

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/fr/photos/skyline-de-la-ville-pendant-la-nuit-phjpsNFw6pM)'
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