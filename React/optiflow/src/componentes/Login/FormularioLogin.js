import './FormularioLogin.css';

function Login() {
  return (
    <div className="login-container">
      <h2>Login</h2>
      <form>

        <label htmlFor="email">E-mail Bosch ou EDV</label>
        <input type="email" id="email" required />

        <label htmlFor="senha">Senha</label>
        <input type="password" id="senha" required />

        <button type="submit">Logar</button>
      </form>
    </div>
  );
}

export default Login;