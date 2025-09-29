---
title: "De l'Utilisation des Métagraphes pour la Vérification de Politiques de Sécurité"

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
publication: In *[23ème Rencontres Francophones sur les Aspects Algorithmiques des Télécommunications](https://apps.univ-lr.fr/cgi-bin/WebObjects/Colloque.woa/wa/menu?code=2721&idMenu=10987&lang=fr) (AlgoTel 2021), La Rochelle*
publication_short: In *AlgoTel 2021*

abstract: "Les processus métier multi-agents aux interactions complexes sont généralement modélisés en tant que workflows. Le propriétaire des données confidentielles interagit avec des sous-traitants pour réaliser une séquence de tâches, en déléguant aux différents acteurs des droits limités sur les données sensibles. Cette délégation repose sur le contrôle d'accès aux données. Pour faciliter sa configuration, les administrateurs proposent une spécification des politiques d'accès et se reposent ensuite souvent sur un traducteur. Cependant, la traduction de la spécification vers l'implémentation peut mener à des erreurs lors d'un déploiement effectif entre les différentes entités du workflow et ainsi engendrer des failles de sécurité. Dans cet article, nous proposons des structures facilitant la détection et la correction d'erreurs potentiellement introduites en raison d'une traduction défectueuse ou d'un déploiement défaillant. En particulier, nous considérons une structure aux fondations formelles capables de modéliser naturellement et surtout très finement les politiques de sécurité : les métagraphes. Nous proposons une suite d'outils de traduction permettant de détecter ces erreurs potentielles et évaluons ses performances."

# Summary. An optional shortened abstract.
summary: []

tags:
  - Vérification de politiques
  - Métagraphes
  - Modélisation de politiques
  - Rego
  - Contrôle d'accès

# Display this page in the Featured widget?
featured: false

# Standard identifiers for auto-linking
hugoblox:
  ids:
    hal: hal-03220092

# Custom links
links:
  # - type: pdf
  #   url: ""
  # - type: code
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  # - type: dataset
  #   url: https://github.com/HugoBlox/hugo-blox-builder
  - type: slides
    url: de-l-utilisation-des-metagraphs-pour-la-verification-de-politiques-de-securite-slides.pdf
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