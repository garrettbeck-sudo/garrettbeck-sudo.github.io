---
layout: default
title: Contact
description: Get in touch with Garrett Beck by email, LinkedIn, or GitHub.
---

<section class="page-hero container">
  <p class="eyebrow">Contact</p>
  <h1>Good work starts with a clear conversation.</h1>
  <p class="lede">Whether you’re working through a complex operating challenge, building something for a community, or just want to compare notes, I’d be glad to hear from you.</p>
</section>

<section class="section container contact-layout" aria-labelledby="contact-title">
  <div class="contact-card">
    <p class="eyebrow">Reach out</p>
    <h2 id="contact-title">Let’s connect.</h2>
    <p>The fastest way to reach me is by email. You can also find my professional background on LinkedIn and my public work on GitHub.</p>
    <a class="contact-email" href="mailto:{{ site.author.email }}">{{ site.author.email }} <span aria-hidden="true">↗</span></a>
    <p class="contact-note">This email address is public. The mail link works best for visitors with an email app configured on their device.</p>
  </div>
  <div class="contact-links" aria-label="Social links">
    <a class="contact-link" href="{{ site.author.linkedin }}">
      <span class="contact-link-label">LinkedIn</span>
      <span>Professional profile <span aria-hidden="true">↗</span></span>
    </a>
    <a class="contact-link" href="https://github.com/{{ site.github_username }}">
      <span class="contact-link-label">GitHub</span>
      <span>@{{ site.github_username }} <span aria-hidden="true">↗</span></span>
    </a>
  </div>
</section>