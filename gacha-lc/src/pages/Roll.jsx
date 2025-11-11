import { useNavigate } from "react-router-dom"

function Roll() {
  const navigate = useNavigate()

  return (
    <>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => navigate("/")}>
          Home
        </button>
      </div>
    </>
  )
}

export default Roll