from fastapi.responses import JSONResponse


def success(data):

    return JSONResponse(

        status_code=200,

        content={

            "success": True,

            "data": data

        }

    )


def failed(message):

    return JSONResponse(

        status_code=400,

        content={

            "success": False,

            "message": message

        }

    )