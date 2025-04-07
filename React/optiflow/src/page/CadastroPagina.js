import Titulo from '../componentes/Titulo/Titulo';
import Cadastro from '../componentes/Cadastro/Formulario';
import BotaoVoltar from '../componentes/BotaoVoltar/Voltar';
import './CadastroPagina.css';

console.log("Renderizou")
function CadastroPagina() {
  return (
    <div className="espacamento-cadastro">
      <div className='botao'>
      <BotaoVoltar />
      </div>
      <Titulo />
      <Cadastro />
      
    </div>
  );
}

export default CadastroPagina;
