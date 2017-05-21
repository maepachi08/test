import sys
sys.path.append("./lib/")
import aws_familiar 


file   = 'pipeline.json'
object = aws_familiar.Pipeline(file)

if object.is_exists():
    print('CodePipeline: ' + object.pipeline_name + ' found.')
    object.get_pipeline()

else:
    print('CodePipeline: ' + object.pipeline_name + ' not found.')

    try:
        object.create()
    except ClientError as err:
        print('CodePipeline: ' + object.pipeline_name + ' create failed.')
    else:
        print('CodePipeline: ' + object.pipeline_name + ' created.')
    finally:
        pass

