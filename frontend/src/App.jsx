import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Navbar from './components/Navbar';
import Comparison from './pages/Comparison';
import Login from './pages/Login';

function App() {
  

  return (
    <div>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/comparison" element={<Comparison/>}/>
          <Route path="/login" element={<Login/>}/>
          <Route path="/" element={<Home />} />
        </Routes>
      </Router>
      
    </div>
  );
}

export default App;