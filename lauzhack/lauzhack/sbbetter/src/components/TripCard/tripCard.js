import { useState } from 'react';
import './tripCard.css'

const TripCard = ({from, to, time, selected = false, onClick, legs, carbon, price, distance}) => {
    return (
        <div className={selected ? "selected" : ""}>
            <sbb-card size="xxxl" color="milk" class={`trip-item-card`} onClick={() => onClick()}>
                <div className="trip-card">
                    <p class="sbb-text-xs co-consumption">{carbon} g <sbb-icon name="cloud-co2-small"></sbb-icon></p>
                    <sbb-journey-header origin={from} destination={to} level="1" size="m"></sbb-journey-header>
                    <p class="sbb-text-s">{distance} km | {Math.floor(time / 60)}h {time % 60}m | {price} CHF</p>
                    <sbb-pearl-chain-time arrival-time={new Date(legs[legs.length - 1].end.time)} departure-time={new Date(legs[0].start.time)} data-now={Math.floor(Date.now() / 1000)} departure-walk="5" arrival-walk="5" legs={legs}></sbb-pearl-chain-time>
                </div>
            </sbb-card>
        </div>
     );
}
 
export default TripCard;