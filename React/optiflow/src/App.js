import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './page/LoginPagina';
import Cadastro from './page/CadastroPagina';
import Monitoramento from './page/MonitoramentoPagina';

function App() {
    return (
      <Routes>
        <Route path="/" element={<Monitoramento />} />
        <Route path="/login" element={<Login />} />
        <Route path="/cadastro" element={<Cadastro />} />
      </Routes>
    );
}

export default App;
