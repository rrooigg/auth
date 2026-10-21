import { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContent";

const Register = () => {
  const [ formData, setFormData ] = useState({
    username:'',
    email:'',
    password:''

  });
  const { register } = useContext(AuthContext);

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value });

  };

  const handleSubmit = (e) => {
    e.preventDefault();
    register(formData.username, formData.email, formData.password);

  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="username" placeholder="Enter your username..." onChange={handleChange}/>
      <input type="email" name="email" placeholder="Enter your email..." onChange={handleChange}/>
      <input type="password" name="password" placeholder="Enter your password..." onChange={handleChange}/>

      <button type="submit">Register</button>
    </form>
  );

};

export default Register
