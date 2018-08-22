import React from 'react'
import './Response.css'

const Errors = (props) => {
    console.log(props)
    let list = <p>There are errors present.</p>
    if (props.err.time) {
        list = <div className="failure" key={props.err.time}>The date was improperly formatted. Please re-read the instructions for proper date formatting.</div>
    }
    if (props.err.data_models) {
        list = <div className="failure" key={props.err.data_models}>{props.err.data_models} does not exist within the data models that would work for this query. Try another data model!</div>
    }
    if (props.err.date_filter) {
        list = <div className="failure" key={props.err.date_filter}>{props.err.date_filter} does not exist within the range of dates that work for this query. Please try again with dates that fit this range.</div>
    }
    return (
       <div className="space_box">
           {list}
       </div> 
    )
}

export default Errors