# GitHub Pages Site - Setup Instructions

This document explains how to activate and use the GitHub Pages site for this repository.

## 🚀 Activation Steps

After merging this PR, follow these steps to activate GitHub Pages:

1. **Go to Repository Settings**
   - Navigate to `Settings` tab in the repository
   - Click on `Pages` in the left sidebar

2. **Configure Source**
   - Under "Build and deployment"
   - Source: Select `Deploy from a branch`
   - Branch: Select `main`
   - Folder: Select `/ (root)`
   - Click `Save`

3. **Wait for Deployment**
   - GitHub will automatically build and deploy the site
   - This usually takes 1-2 minutes
   - You'll see a green checkmark when ready

4. **Access Your Site**
   - The site will be available at: `https://guipetav.github.io/inventario-parque-tecnologico/`
   - A link will also appear in the Pages settings

## 📁 Files Structure

```
/
├── index.html              # Main homepage
├── styles.css              # All styling
├── _config.yml             # Jekyll configuration
├── docs/                   # Documentation (existing)
├── excel/                  # Excel templates (existing)
├── powerbi/                # Power BI materials (existing)
├── scripts/                # Automation scripts (existing)
├── exercicios/             # Exercises (existing)
└── dados-exemplo/          # Sample data (existing)
```

## 🎨 Design System

### Colors
- **Primary**: #003366 (Dark Blue)
- **Secondary**: #0066CC (Medium Blue)
- **Accent**: #FF6B35 (Orange)
- **Success**: #28A745 (Green)
- **Background**: #F8F9FA (Light Gray)

### Typography
- **Font Family**: 'Segoe UI', Roboto, sans-serif
- **Base Size**: 16px
- **Headings**: 24px - 48px

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## 🔧 Customization

### Updating Content

**To update the homepage:**
- Edit `index.html` directly
- All sections are clearly commented
- Changes will be reflected after commit and push

**To update styles:**
- Edit `styles.css`
- Uses CSS variables for easy theming (see `:root` section)
- Mobile-first responsive design

**To change Jekyll theme:**
- Edit `_config.yml`
- Change the `theme:` line to another Jekyll theme
- See available themes: https://pages.github.com/themes/

### Adding New Pages

Create new `.html` or `.md` files in the root or subdirectories:

```html
<!-- new-page.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>New Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Your content -->
</body>
</html>
```

Then link to it from `index.html`:
```html
<a href="new-page.html">New Page</a>
```

## ✨ Features

### Implemented
- ✅ Fully responsive design (mobile, tablet, desktop)
- ✅ Smooth scroll navigation
- ✅ SEO optimized (meta tags, Open Graph)
- ✅ Accessible (ARIA labels, semantic HTML, keyboard navigation)
- ✅ Modern card-based UI with hover effects
- ✅ Professional color scheme
- ✅ Fast loading (pure HTML/CSS, minimal JS)

### JavaScript Features
- Smooth scrolling to anchor links
- Dynamic copyright year
- Sticky header with shadow on scroll

## 🧪 Testing Locally

To test the site locally before pushing:

```bash
# Using Python's built-in server
cd /path/to/repository
python3 -m http.server 8080

# Then open browser to http://localhost:8080
```

Or use any other static file server:

```bash
# Using npx
npx serve

# Using PHP
php -S localhost:8080
```

## 🔍 SEO & Social Media

The site includes:
- **Meta description**: For search engines
- **Keywords**: Relevant to IT asset management
- **Open Graph tags**: For social media sharing
- **Semantic HTML5**: For better SEO

When sharing on social media, the link preview will show:
- Title: "Inventário de Parque Tecnológico"
- Description: "Material didático completo para gestão de ativos de TI"

## ♿ Accessibility

Following WCAG 2.1 AA standards:
- Semantic HTML5 structure
- ARIA labels on interactive elements
- Proper heading hierarchy
- Keyboard navigation support
- Focus indicators
- Sufficient color contrast
- Reduced motion support

## 📱 Browser Compatibility

Tested and working on:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🐛 Troubleshooting

### Site not loading
- Check GitHub Pages settings are correct
- Ensure branch is set to `main`
- Wait a few minutes for deployment
- Check repository Actions tab for build errors

### Styles not applying
- Clear browser cache
- Check `styles.css` is in root directory
- Verify `<link>` tag in `index.html`

### Links not working
- Ensure linked files exist in repository
- Check file paths are relative
- GitHub Pages is case-sensitive

## 📊 Analytics (Optional)

To add Google Analytics:

1. Get your GA tracking ID
2. Add before `</head>` in `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_TRACKING_ID');
</script>
```

## 🔐 Security

- No external dependencies (except Google Fonts via system fonts)
- No user input or forms
- All links use relative paths
- No inline JavaScript in HTML (except initialization)
- HTTPS enforced by GitHub Pages

## 📝 Maintenance

### Regular Updates
- Update copyright year (automatic via JavaScript)
- Review links to ensure they still work
- Update content as course materials change
- Test on new browser versions

### Monitoring
- Check GitHub Pages build status
- Monitor repository Issues for user feedback
- Review analytics (if configured)

## 🤝 Contributing

To contribute improvements to the site:

1. Fork the repository
2. Create a feature branch
3. Make your changes to `index.html` or `styles.css`
4. Test locally
5. Submit a Pull Request

## 📞 Support

If you encounter issues:
- Check this documentation first
- Review GitHub Pages documentation
- Open an issue in the repository
- Contact repository maintainer

---

**Last Updated**: January 2026  
**Version**: 1.0  
**Maintainer**: GUIPETAV
