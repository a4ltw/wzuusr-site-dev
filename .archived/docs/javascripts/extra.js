// Make heading text itself an anchor link
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.md-content h1[id], .md-content h2[id], .md-content h3[id], .md-content h4[id]').forEach(function (heading) {
    var id = heading.id;
    var permalink = heading.querySelector('.headerlink');

    // Wrap text nodes and inline elements (excluding the permalink symbol) in an <a>
    var link = document.createElement('a');
    link.href = '#' + id;
    link.className = 'heading-anchor';

    var nodes = Array.from(heading.childNodes).filter(function (n) {
      return !n.classList || !n.classList.contains('headerlink');
    });
    nodes.forEach(function (n) { link.appendChild(n); });
    heading.insertBefore(link, heading.firstChild);

    // Hide the ¶ permalink symbol
    if (permalink) permalink.style.display = 'none';
  });
});
