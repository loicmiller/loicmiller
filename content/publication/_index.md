---
title: Papers
summary: My publications
type: landing

cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true

sections:
  # - block: collection
  #   id: papers
  #   content:
  #     title: Featured Publications
  #     filters:
  #       folders:
  #         - publication
  #       featured_only: true
  #   design:
  #     view: article-grid
  #     columns: 2
  - block: collection
    content:
      title: Recent publications
      count: 3
      text: ''
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: publication
    content:
      title: Papers
      count: 100
      filters:
        folders:
          - publication
    design:
      view: article-grid
      columns: 2
---
