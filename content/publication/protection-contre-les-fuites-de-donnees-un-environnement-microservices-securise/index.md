---
title: "Protection contre les fuites de données: un environnement micro-services sécurisé"

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

date: '2021-08-07T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2021-08-07T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *[6ème Rencontres Francophones sur la Conception de Protocoles, l’Evaluation de Performance et l’EXpérimentation des Réseaux de Communication](https://apps.univ-lr.fr/cgi-bin/WebObjects/Colloque.woa/wa/menu?code=2721&idMenu=10988&lang=fr) (CoRes 2021), La Rochelle*
publication_short: In *CoRes 2021*

abstract: "Les fuites de données au repos sont malheureusement courantes et en augmentation, entrainant des pertes de profits pour les entreprises ou le non-respect de confidentialité de données personnelles sensibles. La récente montée en puissance des micro-services, en tant que paradigme de déploiement extensible, impose également la sécurisation du trafic. Un processus métier peut être modélisé sous la forme d'un workflow : le propriétaire des données interagit avec des sous-traitants pour réaliser une séquence de tâches. Dans cet article, nous montrons comment ces workflows peuvent être appliqués tout en limitant l'exposition des données. En suivant les principes du zero-trust, nous proposons une infrastructure utilisant l'isolation fournie par les micro-services pour mettre en oeuvre un workflow, dans une preuve de concept disponible en ligne. Nous vérifions ensuite que les politiques de sécurité sont correctement appliquées, et estimons le coût supplémentaire induit par les dispositifs de sécurité."

# Summary. An optional shortened abstract.
summary: []

tags:
  - Fuites de données
  - Workflow
  - Microservices
  - Sécurité

# Display this page in the Featured widget?
featured: false

# Standard identifiers for auto-linking
hugoblox:
  ids:
    hal: hal-03220098

# Custom links
links:
  # - type: pdf
  #   url: ""
  # - type: code
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: dataset
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  - type: slides
    url: protection-contre-les-fuites-de-donnees-un-environnement-microservices-securise-slides.pdf
  # - type: source
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: video
  #   url: https://youtube.com

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/fr/photos/batiment-en-beton-brun-pres-dun-plan-deau-sous-un-ciel-nuageux-pendant-la-journee-bMbRswbmIp0)'
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