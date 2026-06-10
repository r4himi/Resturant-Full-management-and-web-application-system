// ================================
// Language Dropdown Toggle
// ================================
document.addEventListener("DOMContentLoaded", () => {
  const langBtn = document.getElementById("langBtn");
  const dropdown = document.querySelector(".dropdown-content");

  langBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    dropdown.style.display =
      dropdown.style.display === "block" ? "none" : "block";
  });

  // Close dropdown when clicking outside
  window.addEventListener("click", (e) => {
    if (!e.target.closest(".language-dropdown")) {
      dropdown.style.display = "none";
    }
  });

  // Load saved language on page load
  const savedLang = localStorage.getItem("selectedLanguage");
  const savedName = localStorage.getItem("languageName");

  if (savedLang && savedName) {
    selectLanguage(savedLang, savedName);
  }
});

// ================================
// Language Selection & Translation
// ================================
function selectLanguage(langCode, displayName) {
  // Save language
  localStorage.setItem("selectedLanguage", langCode);
  localStorage.setItem("languageName", displayName);

  // Update language button text
  document.getElementById("langBtn").innerText = displayName;

  // Close dropdown
  document.querySelector(".dropdown-content").style.display = "none";

  // ================================
  // RTL / LTR Support
  // ================================
  if (langCode === "fa") {
    document.documentElement.setAttribute("dir", "rtl");
    document.body.classList.add("rtl");
  } else {
    document.documentElement.setAttribute("dir", "ltr");
    document.body.classList.remove("rtl");
  }

  // ================================
  // Translations
  // ================================
  const translations = {
    en: {
      title: "BigBurgers",
      slogan: "Bite into Happiness",
      reserveBtn: "Reserve Your Table Now",
      footerName: "BigBurgers",
      footerSlogan: "Bite into Happiness",
      navHome: "Home",
      navMenu: "Menu",
      navAbout: "About Us",
      navContact: "Contact Us"
    },
    fa: {
      title: "بیگ برگرز",
      slogan: "یک لقمه خوشبختی",
      reserveBtn: "رزرو میز شما",
      footerName: "بیگ برگرز",
      footerSlogan: "یک لقمه خوشبختی",
      navHome: "خانه",
      navMenu: "منو",
      navAbout: "درباره ما",
      navContact: "تماس با ما"
    },
    es: {
      title: "BigBurgers",
      slogan: "Muerde la Felicidad",
      reserveBtn: "Reserva Tu Mesa Ahora",
      footerName: "BigBurgers",
      footerSlogan: "Muerde la Felicidad",
      navHome: "Inicio",
      navMenu: "Menú",
      navAbout: "Sobre Nosotros",
      navContact: "Contacto"
    }
  };

  const t = translations[langCode];

  // ================================
  // Apply Translations
  // ================================
  document.querySelector(".the-name").innerText = t.title;
  document.querySelector(".solgan").innerText = t.slogan;
  document.querySelector(".category-btn").innerText = t.reserveBtn;

  // Navbar
  const navLinks = document.querySelectorAll(".nav-list li a");
  navLinks[0].innerText = t.navHome;
  navLinks[1].innerText = t.navMenu;
  navLinks[2].innerText = t.navAbout;
  navLinks[3].innerText = t.navContact;

  // Footer brand
  document.querySelector(".footer-container .brand-name h3").innerText =
    t.footerName;
  document.querySelector(".footer-container .brand-name p").innerText =
    t.footerSlogan;

  // Footer nav
  const footerLinks = document.querySelectorAll(
    ".footer-container .nav-links li a"
  );
  footerLinks[0].innerText = t.navHome;
  footerLinks[1].innerText = t.navMenu;
  footerLinks[2].innerText = t.navAbout;
  footerLinks[3].innerText = t.navContact;
}
