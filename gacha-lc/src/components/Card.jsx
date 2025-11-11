import "./Card.css";
// import companyLogo from "../assets/google.svg"

function Card({image}) {

  return (
    <div className = "box">
        <img src={image} alt="company" className="box-image"/>
    </div>
  )
}

export default Card;
