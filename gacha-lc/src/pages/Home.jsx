import { useNavigate } from "react-router-dom"

function Home() {
  const navigate = useNavigate()

  return (
    <>
      <h1>Home page</h1>
      <div className="rollmenu">
        <h3>Roll options</h3>
        <button onClick={() => navigate("/roll")}>
          Roll x3
        </button>
      </div>
    </>
  )
}

export default Home
