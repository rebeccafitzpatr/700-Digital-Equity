import React from 'react';

export default function ListItem({ record }){
  return (
    <li className="list-item">
      <div className="list-item-content">
      <span>{record.name}</span>
        <span>{record.region}</span>
        <span>{record.latency} ms</span>
        <span>{record.upload} MB/s</span>
        <span>{record.download} MB/s</span>
        <span>{record.device}</span>
      </div>
    </li>
  );
};
