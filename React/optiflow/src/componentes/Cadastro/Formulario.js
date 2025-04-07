import './Formulario.css';

function Cadastro() {
  return (
    <div className="cadastro-container">
      <h2>Cadastro</h2>
      <form>
        <label htmlFor="nome">Nome do colaborador</label>
        <input type="text" id="nome" required />

        <label htmlFor="email">E-mail Bosch ou EDV</label>
        <input type="email" id="email" required />

        <label htmlFor="senha">Senha</label>
        <input type="password" id="senha" required />

        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
}

export default Cadastro;
