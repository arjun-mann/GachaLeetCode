import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from "./pages/Home"
import Roll from "./pages/Roll"
import Inventory from "./pages/Inventory"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/roll" element={<Roll/>}/>
        <Route path="/inventory" element={<Inventory/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
