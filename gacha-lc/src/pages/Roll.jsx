import { useNavigate } from "react-router-dom"
import Card from "../components/Card"
import "./Roll.css";
import googleLogo from "../assets/google.svg"
import amazonLogo from "../assets/amazon.svg"
import appleLogo from "../assets/apple.svg"
import facebookLogo from "../assets/facebook.svg"


function Roll() {
  const navigate = useNavigate();
  const allCards = [
    {
      image: googleLogo
    },
    {
      image: amazonLogo
    },
    {
      image: appleLogo
    },
    {
      image: facebookLogo
    }
  ];

  const getRandomCards = (arr, count) => {
    const shuffled = [...arr].sort(() => Math.random() - .5);
    return shuffled.slice(0, count)
  };

  const randomCards = getRandomCards(allCards, 3);

  return (
    <>
      <h1>Vite + React</h1>
      <div>
        <button onClick={() => navigate("/")}>
          Home
        </button>
        <div className="roll-grid">
          {randomCards.map((card) => (
            <Card image={card.image}/>
          ))}
        </div>
      </div>
    </>
  )
}

export default Roll