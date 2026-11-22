
import { useState } from "react";
import "./App.css";

type Page = "home" | "team";

const teamMembers = [
  {
    name: "Mohamed Nizar Madih",
    initials: "NM",
    image: "/team/nizar.png",
    linkedin: "https://www.linkedin.com/in/mohamed-nizar-madih/",
  },
  {
    name: "Ilyas Harti",
    initials: "IH",
    image: "/team/ilyas.jpg",
    linkedin: "https://www.linkedin.com/in/ilyasharti/",
  },
  {
    name: "Abderrahim Azeroual",
    initials: "AA",
    image: "/team/azeroual.jpg",
    linkedin: "https://www.linkedin.com/in/abderrahimazeroual/",
  },
  {
    name: "Amine Koula",
    initials: "AK",
    image: "/team/amine.png",
    linkedin: "https://www.linkedin.com/in/amine-koula/",
  },
];

function App() {
  const [page, setPage] = useState<Page>("home");
  const [message, setMessage] = useState("");

  function navigate(nextPage: Page) {
    setPage(nextPage);
    window.scrollTo(0, 0);
  }

  return (
    <div className="app">
      <header className="navbar">
        <button
          className="brand-button"
          onClick={() => navigate("home")}
        >
          ✦ IntelliRetouch
        </button>

        <nav className="nav-links" aria-label="Navigation principale">
          <button
            className={page === "home" ? "nav-active" : ""}
            onClick={() => navigate("home")}
          >
            Accueil
          </button>
          <button
            className={page === "team" ? "nav-active" : ""}
            onClick={() => navigate("team")}
          >
            Notre équipe
          </button>
        </nav>
      </header>

      {page === "home" ? (
        <main className="hero" id="home">
          <span className="eyebrow">
            LA RETOUCHE RÉINVENTÉE
          </span>

          <h1>
            Vos photos,
            <br />
            <span>sans distractions.</span>
          </h1>

          <p>
            Effacez les éléments indésirables de vos images
            et retrouvez des photos naturellement parfaites.
          </p>

          <button
            className="primary-button"
            onClick={() =>
              setMessage(
                "Bienvenue ! Votre espace de retouche sera bientôt disponible."
              )
            }
          >
            Commencer la retouche →
          </button>

          {message && (
            <div className="message">{message}</div>
          )}
        </main>
      ) : (
        <main className="team-page">
          <span className="eyebrow">LES VISAGES DERRIÈRE L'INNOVATION</span>

          <h1>
            Rencontrez <span>notre équipe.</span>
          </h1>

          <p className="team-intro">
            Une équipe passionnée qui imagine des expériences
            de retouche photo plus simples et plus intuitives.
          </p>

          <div className="team-grid">
            {teamMembers.map((member) => (
              <article className="member-card" key={member.linkedin}>
              <img
                src={member.image}
                alt={`Photo de ${member.name}`}
                className="member-avatar"
                loading="lazy"
              />

                <h2>{member.name}</h2>

                <p>Membre de l'équipe IntelliRetouch</p>

                <a
                  href={member.linkedin}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="linkedin-link"
                  aria-label={`Contacter ${member.name} sur LinkedIn`}
                >
                  <span className="linkedin-mark">in</span>
                  Voir le profil LinkedIn ↗
                </a>
              </article>
            ))}
          </div>

          <section className="contact-section">
            <h2>Une question ? Une idée ?</h2>
            <p>
              Nous serions ravis d'échanger avec vous.
              Contactez un membre de notre équipe sur LinkedIn
              pour discuter, partager vos retours ou en savoir plus.
            </p>
            <a
              href={teamMembers[0].linkedin}
              target="_blank"
              rel="noopener noreferrer"
              className="primary-button contact-button"
            >
              Contacter notre équipe ↗
            </a>
          </section>
        </main>
      )}

      <footer>
        © 2026 IntelliRetouch. Tous droits réservés.
      </footer>
    </div>
  );
}

export default App;
