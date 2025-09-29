---
title: Mining in Logarithmic Space with Variable Difficulty

event: ACM Conference on Computer and Communications Security
event_url: https://www.sigsac.org/ccs/CCS2025/

location: Taipei International Convention Center
address:
  street: No. 1, Section 5, Xinyi Rd
  city: Taipei City
  region: Xinyi District
  postcode: 110
  country: Taïwan

summary: []
abstract: "This paper presents the first non-interactive, succinct, and secure representation of a PoW-based blockchain that operates under variable mining difficulty while satisfying both completeness and onlineness properties. Completeness ensures that provers can update an existing NIPoPoW by incorporating a newly mined block, whereas onlineness ensures that miners can extend the chain directly from a NIPoPoW. The time complexity for both the prover (to update a NIPoPoW with a new block) and the verifier is logarithmic in the number of blocks of the underlying PoW blockchain. The communication complexity required for synchronization is polylogarithmic in the length of the blockchain. We prove the correctness of our scheme in the presence of a 1/3-bounded PPT adversary."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2025-10-14T14:00:00Z'
date_end: '2025-10-14T14:15:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2025-09-28T00:00:00Z'

authors:
  - admin
  - Dorian Pacaud
  - Nathanaël Derousseaux--Lebert
  - Emmanuelle Anceaume
  - Romaric Ludinard

tags:
  - Blockchain
  - Variable difficulty
  - Succinct proof
  - Polylogarithmic communication and update complexities

# Is this a featured talk? (true/false)
featured: false

image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/fr/photos/skyline-de-la-ville-pendant-la-nuit-phjpsNFw6pM)'
  focal_point: ''

links:
  # - type: code
  #   url: https://github.com
  # - type: slides
  #   url: mining-in-logarithmic-space-with-variable-difficulty-slides.pdf
  # - type: video
  #   url: https://youtube.com

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---