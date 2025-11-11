import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import Home from "./pages/Home"
import Roll from "./pages/Roll"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/roll" element={<Roll/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
