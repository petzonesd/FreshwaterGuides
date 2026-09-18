# Freshwater Guides

Initial static launch site for [freshwaterguides.com](https://freshwaterguides.com).

## Publish with GitHub Pages

1. In the GitHub repository, go to **Settings → Pages**.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Select branch `main` and folder `/ (root)`, then save.
4. GitHub will publish the repository at its GitHub Pages URL.
5. In **Settings → Pages**, set the custom domain to `freshwaterguides.com` and enable **Enforce HTTPS** once DNS verification is complete.

## GoDaddy DNS records

At GoDaddy, open the DNS tab for `freshwaterguides.com` and add the four GitHub Pages A records below for the apex domain (`@`):

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

Add a CNAME record:

```
Host: www
Points to: petzonesd.github.io
```

Remove conflicting A, AAAA, or CNAME records for `@` and `www`. DNS changes and HTTPS provisioning can take time to propagate.

## Site editing

- `index.html` contains the launch homepage.
- `styles.css` contains all site styling.
- Add future guides as standalone HTML pages, then add their URLs to `sitemap.xml`.
- Keep content original, practical, and transparently disclose affiliated-business links where they appear.
