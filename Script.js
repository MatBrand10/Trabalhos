const users = [
  {
    photo: 'https://randomuser.me/api/portraits/men/75.jpg',
    name: 'João Silva',
    semester: 4,
    course: 'Engenharia de Software',
    bio: 'Apaixonado por tecnologia e desenvolvimento.',
    interests: ['JavaScript', 'React', 'Node.js', 'Design'],
  },
  {
    photo: 'https://randomuser.me/api/portraits/women/65.jpg',
    name: 'Maria Oliveira',
    semester: 3,
    course: 'Design Gráfico',
    bio: 'Criativa e amante de artes visuais.',
    interests: ['Photoshop', 'Illustrator', 'UI/UX'],
  },
  {
    photo: 'https://randomuser.me/api/portraits/men/80.jpg',
    name: 'Carlos Souza',
    semester: 2,
    course: 'Administração',
    bio: '',
    interests: ['Marketing', 'Vendas'],
  },
];

let currentIndex = 0;
let likedUsers = [];
let passedUsers = [];

const loginSection = document.getElementById('login-section');
const profileSection = document.getElementById('profile-section');
const profileStackContainer = document.getElementById('profile-stack-container');
const noMoreProfilesSection = document.getElementById('no-more-profiles');
const loginForm = document.getElementById('login-form');
const passBtn = document.getElementById('pass-btn');
const likeBtn = document.getElementById('like-btn');
const toggleThemeBtn = document.getElementById('toggle-theme');


let dragging = false, startX = 0, currentCard = null, offsetX = 0;
function createSwipeCard(user, idx) {
  const card = document.createElement('div');
  card.className = 'swipe-card shadow';
  if (idx === currentIndex) card.classList.add('top');
  if (idx === currentIndex + 1) card.classList.add('next');
  card.innerHTML = `
    <img class="photo" src="${user.photo}" alt="${user.name}"/>
    <div class="swipe-card-info">
      <div class="swipe-card-name">${user.name}</div>
      <div class="swipe-card-course">${user.semester}º semestre - ${user.course}</div>
      ${user.bio ? `<div class="swipe-card-bio">${user.bio}</div>` : ''}
      <div class="swipe-card-interests">
        ${user.interests.map(t => `<span class="swipe-card-interest-tag">${t}</span>`).join('')}
      </div>
    </div>
  `;
  card.addEventListener('pointerdown', e => {
    if (idx !== currentIndex) return;
    dragging = true;
    startX = e.clientX || e.touches?.[0]?.clientX;
    currentCard = card;
    card.setPointerCapture(e.pointerId);
  });
  card.addEventListener('pointermove', e => {
    if (!dragging || idx !== currentIndex) return;
    offsetX = (e.clientX || e.touches?.[0]?.clientX) - startX;
    card.style.transform = `translateX(${offsetX}px) rotate(${offsetX/13}deg)`;
  });
  card.addEventListener('pointerup', e => {
    if (!dragging || idx !== currentIndex) return;
    dragging = false;
    if (offsetX > 110) { likeUser(); }
    else if (offsetX < -110) { passUser(); }
    else {
      card.style.transition = 'transform 0.18s'; card.style.transform = '';
      setTimeout(() => { card.style.transition = ''; }, 180);
    }
    offsetX = 0;
  });
  return card;
}
function renderProfileStack() {
  profileStackContainer.innerHTML = '';
  if (currentIndex >= users.length) {
    showNoMoreProfiles();
    return;
  }
  for (let i = users.length - 1; i >= currentIndex; i--) {
    const card = createSwipeCard(users[i], i);
    if (i - currentIndex <= 1) profileStackContainer.appendChild(card);
  }
}
function likeUser() {
  if (currentIndex >= users.length) return;
  likedUsers.push(users[currentIndex]);
  animateCard('right');
  currentIndex++;
  setTimeout(renderProfileStack, 220);
}
function passUser() {
  if (currentIndex >= users.length) return;
  passedUsers.push(users[currentIndex]);
  animateCard('left');
  currentIndex++;
  setTimeout(renderProfileStack, 220);
}
function animateCard(direction) {
  const card = document.querySelector('.swipe-card.top');
  if (card) {
    card.style.transition = 'transform 0.22s cubic-bezier(.6,1.7,.8,.98)';
    card.style.transform = direction === 'right'
      ? 'translateX(420px) rotate(16deg)' : 'translateX(-420px) rotate(-17deg)';
  }
}
function showNoMoreProfiles() {
  profileSection.classList.add('d-none');
  noMoreProfilesSection.classList.remove('d-none');
  noMoreProfilesSection.innerHTML = `
    <div class="no-more-profiles-container">
      <img src="https://cdn-icons-png.flaticon.com/512/1180/1180346.png" alt="Sem mais perfis" />
      <h3 class="title">Sem mais perfis</h3>
      <p class="subtitle">Volte mais tarde para encontrar novos matches.</p>
    </div>`;
}

loginForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value.trim();
  if (username && password) {
    loginSection.classList.add('d-none');
    profileSection.classList.remove('d-none');
    noMoreProfilesSection.classList.add('d-none');
    currentIndex = 0;
    renderProfileStack();
  } else {
    alert('Preencha usuário e senha');
  }
});

passBtn.addEventListener('click', () => passUser());
likeBtn.addEventListener('click', () => likeUser());

toggleThemeBtn.addEventListener('click', () => {
  if (document.body.classList.contains('dark')) {
    document.body.classList.remove('dark');
    toggleThemeBtn.innerHTML = '<i class="fa fa-moon"></i>';
  } else {
    document.body.classList.add('dark');
    toggleThemeBtn.innerHTML = '<i class="fa fa-sun"></i>';
  }
});
