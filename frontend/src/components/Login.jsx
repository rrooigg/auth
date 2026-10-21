import { useState, useContext } from "react";
import { AuthContext } from '../context/AuthContent';

const Login = () => {
  const [ formData, setFormData ] = useState({
    username: '',
    password: ''

  });
  const { login } = useContext(AuthContext);

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value });

  };

  const handleSubmit = (e) => {
    e.preventDefault();
    login(formData.username, formData.password);

  };

  return(
    <form onSubmit={handleSubmit}>
      <input type="text" name="username" placeholder="Enter your username..." onChange={handleChange}/>
      <input type="password" name="password" placeholder="Enter your password..." onChange={handleChange}/>

      <button type="submit">Login</button>

    </form>
  );

};

export default Login