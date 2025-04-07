import './Navbar.css'
import { Link } from 'react-router-dom';



export default function Navbar() {
    return (
        <nav className="navbar">     
        <img src="/imagens/logo.png" alt="Logo Bosch" className="navbar-img" />
       
        
        <div className="navbar-menu">
        <Link className="navbar-link" to="/login">Login</Link>
        <Link className="navbar-link" to="/cadastro">Cadastro</Link>
        <Link className="navbar-link" to="/">Monitoramento</Link>
        </div>
        <div className='imagem-opti'>
          <img src='/imagens/opti_text.png' alt='Logo Optiflow'></img>
        </div>
      </nav>      
    );
  }
  