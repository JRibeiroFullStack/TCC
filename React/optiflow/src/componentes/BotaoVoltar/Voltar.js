import './Voltar.css'


function BotaoVoltar() {
    const handleClick = () => {
      window.history.back(); 
    };
  
    return (
      <button onClick={handleClick} className="botao-voltar">
        <span className="seta">&#8592;</span>
      </button>
    );
  }
export default BotaoVoltar