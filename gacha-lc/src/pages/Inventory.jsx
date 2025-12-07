import { useNavigate } from "react-router-dom"

function Inventory() {
    const navigate = useNavigate()
    return (
        <>
            <h1>Inventory Page</h1>
            <div classname = "inventorymenu">
                <h3>Cards obtained</h3>
                <button onClick = {() => navigate("/")}>
                    Home
                </button>
            </div>
        </>
    )
}

export default Inventory
