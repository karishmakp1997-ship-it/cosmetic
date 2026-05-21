
// ===================== LUXURY DIAGONAL =====================
function initLuxury() {
  const imgs = document.querySelectorAll('.luxury-img');
  if (imgs.length < 2) return;

  // Initial setup
  imgs[0].style.opacity = '1';
  imgs[0].style.zIndex = '2';
  imgs[1].style.opacity = '0.3';
  imgs[1].style.zIndex = '1';

  let current = 0;

  setInterval(() => {
    const curr = imgs[current];
    const next = imgs[(current + 1) % imgs.length];

    // Both visible — curr fades to back, next comes to front
    curr.style.transition = 'opacity 1s ease, z-index 0s';
    next.style.transition = 'opacity 1s ease, z-index 0s';

    curr.style.opacity = '0.3';  // stays visible but dimmed
    curr.style.zIndex = '1';

    next.style.opacity = '1';    // comes to front bright
    next.style.zIndex = '2';

    current = (current + 1) % imgs.length;
  }, 2000);
}
initLuxury();
// ===================== CATEGORIES SLIDER =====================
let catOffset = 0;
const CAT_VISIBLE = 4;

function catMove(dir) {
  const track = document.getElementById('categoriesTrack');
  if (!track) return;
  const total = track.children.length;
  const max = Math.max(0, total - CAT_VISIBLE);
  catOffset = Math.max(0, Math.min(catOffset + dir, max));
  updateCatPosition();
}
function updateCatPosition() {
  const track = document.getElementById('categoriesTrack');
  if (!track || !track.children.length) return;
  const cardW = track.children[0].offsetWidth + 20;
  track.style.transform = `translateX(-${catOffset * cardW}px)`;
}

// ===================== WHY GLOWIFY ANIMATION =====================
function initWhyAnimation() {
  const points = document.querySelectorAll('.why-point');
  if (!points.length) return;

  let idx = 0;
  function revealNext() {
    if (idx < points.length) {
      points[idx].classList.add('revealed');
      idx++;
      setTimeout(revealNext, 450);
    } else {
      setTimeout(() => {
        points.forEach(p => p.classList.remove('revealed'));
        idx = 0;
        setTimeout(revealNext, 600);
      }, 3000);
    }
  }

  const obs = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      revealNext();
      obs.disconnect();
    }
  }, { threshold: 0.3 });

  const whySection = document.getElementById('whySection');
  if (whySection) obs.observe(whySection);
}
initWhyAnimation();

// ===================== CUSTOMERS SLIDER =====================
let custIdx = 0;
const customerTrack = document.getElementById('customerTrack');
const custDotEls = document.querySelectorAll('.cust-dot');

function custMove(dir) {
  const cards = document.querySelectorAll('.customer-card');
  if (!cards.length) return;
  custIdx = (custIdx + dir + cards.length) % cards.length;
  updateCustPos();
}
function custGoTo(i) {
  custIdx = i;
  updateCustPos();
}
function updateCustPos() {
  if (customerTrack) {
    customerTrack.style.transform = `translateX(-${custIdx * 100}%)`;
  }
  custDotEls.forEach((d, i) => d.classList.toggle('active', i === custIdx));
}
const custCards = document.querySelectorAll('.customer-card');
if (custCards.length > 0) {
  setInterval(() => custMove(1), 5000);
}

// ===================== SEARCH =====================
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

if (searchInput) {
  let searchTimeout;
  searchInput.addEventListener('input', function () {
    clearTimeout(searchTimeout);
    const q = this.value.trim();
    if (!q) {
      searchResults.classList.remove('show');
      return;
    }
    searchTimeout = setTimeout(() => {
      fetch(`/search/?q=${encodeURIComponent(q)}`)
        .then(res => res.json())
        .then(data => {
          if (!data.results.length) {
            searchResults.innerHTML = '<div class="search-item">No results found</div>';
            searchResults.classList.add('show');
            return;
          }
          searchResults.innerHTML = data.results.map(p => `
            <div class="search-item">
              <img src="${p.image}" alt="${p.name}" onerror="this.style.display='none'">
              <div>
                <div style="font-weight:600;color:var(--dark)">${p.name}</div>
                <div style="color:#8a7080">₹${p.price}</div>
              </div>
            </div>
          `).join('');
          searchResults.classList.add('show');
        })
        .catch(() => {
          searchResults.classList.remove('show');
        });
    }, 300);
  });

  document.addEventListener('click', e => {
    if (!e.target.closest('.search-wrapper')) {
      searchResults.classList.remove('show');
    }
  });
}