import { useNavigate } from "react-router-dom"
import Card from "../components/Card"
import "./Roll.css";
import googleLogo from "../assets/google.svg"
import amazonLogo from "../assets/amazon.svg"

function Roll() {
  const navigate = useNavigate()
  const randomCards = [
    {
      image: googleLogo
    },
    {
      image: amazonLogo
    },
    {
      image: googleLogo
    }
  ];


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