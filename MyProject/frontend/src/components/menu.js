import React from 'react';
import './menu.css';

export default function Menu() {
    return (
        <nav className="nav">
            <ul className="menu">
                <li className="menu__item"><a href="">Пункт меню</a></li>
                <li className="menu__item"><a href="">Пункт меню</a></li>
                <li className="menu__item"><a href="">Пункт меню</a></li>
            </ul>
        </nav>
    );
}