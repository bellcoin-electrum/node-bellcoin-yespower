#include <node.h>
#include <node_buffer.h>
#include <v8.h>
#include <nan.h>

extern "C" {
#include "yescrypt-0.5/yescrypt.h"
}

#define THROW_ERROR_EXCEPTION(x) Nan::ThrowError(x)

using namespace node;
using namespace v8;

NAN_METHOD(hash) {
    if (info.Length() < 1) {
        return THROW_ERROR_EXCEPTION("You must provide one argument.");
    }

    Local<Object> target = Nan::To<Object>(info[0]).ToLocalChecked();

    if(!Buffer::HasInstance(target)) {
        return THROW_ERROR_EXCEPTION("Argument should be a buffer object.");
    }

    char *input = Buffer::Data(target);
    char *output = (char*) malloc(sizeof(char) * 32);

    yescrypt_hash(input, output);

    info.GetReturnValue().Set(Nan::NewBuffer(output, 32).ToLocalChecked());
}

NAN_MODULE_INIT(init)
{
    NAN_EXPORT(target, hash);
}

NODE_MODULE(bitzeny_yescrypt, init);

