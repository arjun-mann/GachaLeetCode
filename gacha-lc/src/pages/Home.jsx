import { useNavigate } from "react-router-dom"

function Home() {
  const navigate = useNavigate()

  return (
    <>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => navigate("/roll")}>
          Roll
        </button>
      </div>
    </>
  )
}

export default Home
