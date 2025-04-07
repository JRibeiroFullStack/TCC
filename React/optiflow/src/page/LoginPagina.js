import Titulo from '../componentes/Titulo/Titulo';
import Login from '../componentes/Login/FormularioLogin';
import BotaoVoltar from '../componentes/BotaoVoltar/Voltar';
import './LoginPagina.css';

function LoginPagina() {
  return (
    <div className="espacamento-login">
      <div className='botao'>
      <BotaoVoltar />
      </div>
      <Titulo />
      <Login />
    </div>
  );
}

export default LoginPagina;